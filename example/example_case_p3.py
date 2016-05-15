
# coding: utf-8

# **By:** Ties de Kok and Jan Boone  
# **Python version:** 2.7 but will also work with 3.5 (see notes)

# # example: process files

# The best way to learn Python is by finding a problem that you want to solve using Python.  
# So in this example:
# 
# **Problem:**
# 
# I download a lot of working papers from SSRN but they all end up in my `Downloads` folder with cryptic names like `SSRN-id2645351.pdf`  
# 
# **Desired solution:**  
# 
# I want to write a script to check my `Downloads` folder for SSRN papers and categorize them.

# # prerequisites

# It is a good habit to always:  
# 1. Mention which version of Python you are using
# 2. Put your `imports` at the top of the file
# 3. Define your working directory explicitly 

# ## Imports

# Import some standard libraries that we will be using

# In[1]:

import os, re, time, shutil, pickle, collections


# In[2]:

import urllib


# **Note: ** For Python 3 we need import `urllib` instead of `urllib2`

# To read the contents of PDF files we need a package called `PyPDF2`  
# **Note:** `PyPDF2` is third-party package, so we need to install it first:  
# 1. Open up your command prompt
# 2. Type: `pip install PyPDF2`

# In[3]:

import PyPDF2


# For more complex data structures we use the `pandas` package.  
# This package is pre-installed by the Anaconda distribution.

# In[4]:

import pandas as pd


# ## Define working directory

# It is always a good habit to explicitly define your working directory.  
# This makes it easier to use the code across computers / people. 
# 
# By default the working directory is set to the location of the Notebook.

# In[5]:

os.chdir(r'C:\Stack\Work\Workshops\python_workshop\opensource_workshop\example')


# # scanning a directory

# In[6]:

downloads_path = r'Downloads'


# ### Obtain a list of all the files in a directory

# In[7]:

downloads_files = os.listdir(downloads_path)


# Feel free to interactively check the contents of a variable, for example:

# In[8]:

downloads_files[0:7]


# ### Create a list with all the .pdf files

# There are several ways to do this, REGEX is the most powerful but can be complex.  
# An easier way is to just check whether the final 4 characters equal '.pdf'.  
# 
# For more information on `[-4:]` see the Python cheat sheet.

# In[9]:

pdf_files = []
for i in downloads_files:
    if i[-4:] == '.pdf':
        pdf_files.append(i)


# In[10]:

pdf_files[:5]


# ### Keep only those files that start with 'SSRN'

# In[11]:

ssrn_files = []
for i in pdf_files:
    if i[:4] == 'SSRN':
        ssrn_files.append(i)


# In[12]:

ssrn_files[:5]


# ### Check the number of SSRN files

# In[13]:

len(ssrn_files)


# ## Process the SSRN files

# ### Remove duplicates using `set`

# A `set` is similar to a `list` but only contains unique values.  
# However, when downloading duplicate files the file name is appended by ` (1)` so `set` does not work.

# In[14]:

ssrn_files = set(ssrn_files)
len(ssrn_files)


# ### Remove duplicates using a regular expression

# Regular expression are very powerful to specify patterns but they are complicated to get right.  
# My personal approach is to use trial-and-error, these two websites makes this easier:  
# - [pyregex](http://pyregex.com/)
# - [pythex](http://pythex.org/)

# We want to make sure that the file-name follows a valid pattern.  
# `re.match('SSRN-id\d{5,7}\.pdf', i)` returns `True` if the filename is:  
# - `SSRN-id12345.pdf`
# - `SSRN-id123456.pdf`
# - `SSRN-id1234567.pdf`

# In[15]:

ssrn_unique = [i for i in ssrn_files if re.match('SSRN-id\d{5,7}\.pdf', i)]


# A very powerful and useful feature of Python are the so-called `comprehensions`.  
# Above I used a `list comprehension` as noted by the brackets.  
# 
# Essentially that one-line of code equals:

# In[16]:

ssrn_unique_v2 = []
for i in ssrn_files:
    if re.match('SSRN-id\d{5,7}\.pdf', i):
        ssrn_unique_v2.append(i)


# In[17]:

len(ssrn_unique) == len(ssrn_unique_v2)


# In[18]:

len(ssrn_unique)


# In[19]:

len(ssrn_unique) == len(ssrn_files)


# ## Retrieve the download date for each file

# We can get the creation time using `os.path.getctime()`.  
# To make it human readible we can convert it using `time.ctime()`  
# 
# The most consistent way to dynamically create a path is to use `os.path.join()`:

# In[20]:

os.path.join(downloads_path, ssrn_unique[0])


# In[21]:

ssrn_ctime = {}
for i in ssrn_unique:
    path_file = os.path.join(downloads_path, i)
    ssrn_ctime[i] = os.path.getctime(path_file)


# `ssrn_ctime` is a dictionary. Each item consists of a `key` and a `value`.

# In[22]:

type(ssrn_ctime)


# A dictionary is useful because it allows to retreive the `value` using the `key`:  
# 
# *Note:* `ssrn_unique[0]` simply gets the first item from the `ssrn_unique` list.

# In[23]:

ssrn_ctime[ssrn_unique[0]]


# In[24]:

time.ctime(ssrn_ctime[ssrn_unique[0]])


# # retrieve information about the working paper

# In order to categorize the PDF files we need to obtain some more information about each file.  
# We can get this information from two sources:
# 1. Open the PDF file using `PyPDF2`
# 2. Use the file name to scrape information from the corresponding SSRN page

# ## Open the PDF using PyPDF2

# In[25]:

pdf_file = PyPDF2.PdfFileReader(os.path.join(downloads_path, ssrn_unique[0]))


# In[26]:

print(pdf_file.getPage(0).extractText())


# The problem with PDF files is that they are aimed to be human readable, not machine readable.  
# This is especially problematic given that papers are not consistently formatted.  
# 
# It is, therefore, easier to look for a different source of information.

# ## Retrieve information from the SSRN page

# While the SSRN filename appear cryptic they actually contain a machine readable ID.  
# We can use the ID to construct a URL that leads to the corresponding SSRN webpage.

# For example:  
# The file `SSRN-id2610429.pdf` refers to ID: 2610429  
# We can use this ID to create the SSRN url:  
# http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2610429

# ### Construct a dictionary with the ID for each file

# First step is to extract the ID from the filename.  
# We can do this with a Regular Expression: `'id(\d{5,7})\.pdf'`.  
# 
# *Note:* we use `re.findall()` which always returns a `list`, therefore we add `[0]` to extract the first element

# In[27]:

ssrn_ID = {i : re.findall('id(\d{5,7})\.pdf', i)[0] for i in ssrn_unique}


# *Note:* above I use a dictionary comprehension, this is equal to:

# In[28]:

ssrn_ID = {}
for i in ssrn_unique:
    ssrn_ID[i] = re.findall('id(\d{5,7})\.pdf', i)[0]


# In[29]:

ssrn_ID['SSRN-id2610429.pdf']


# ### Construct URL based on ID

# Below we will loop over a dictionary instead of a list.  
# Every item in a dictionary consists of two components: `key`, `value`.  
# To deal with this we define two variables (`k, v`) in the loop statement.  
# 
# **Note:** In Python 2.7 we have to use `.items()` in Python 3 this has been simplified to `.items()`

# In[30]:

ssrn_url = {}
for k, v in ssrn_ID.items():
    url = 'http://papers.ssrn.com/sol3/papers.cfm?abstract_id=%s' % v
    ssrn_url[k] = url


# In[31]:

ssrn_url['SSRN-id2610429.pdf']


# ### Retrieve information from the webpage

# There are many different ways to extract information from a webpage using Python.  
# Here we will use the most basic version that works fine for simple tasks.  

# We will open a webpage and retrieve the HTML source using the build-in `urllib2` module. 

# In[34]:

url = ssrn_url['SSRN-id2610429.pdf']
html_text = urllib.request.urlopen(url).read().decode('utf-8')


# **Note 1: the urllib library has been substantialy changed in Python 3:**  
# ```
# url = ssrn_url['SSRN-id2610429.pdf']
# html_text = urllib.request.urlopen(url).read().decode('utf-8')
# ```
# 
# **Note 2: if you get a `HTTP Error 503` --> Just try again.**

# More advanced HTML parsers such as `BeautifulSoup` allow you to select components based on their characteristics.  
# For this example we are going to use the easiest way and use Regular Expressions instead.  
# 
# We are interested in the following items:  
# 1. title
# 2. author
# 3. publication date
# 
# If you check the HTML page source you will observe that these are included between `meta` tags:
# 
#     <title>Financial Accounting Research, Practice, and Financial Accountability by Mary E. Barth :: SSRN</title>
#    
#     <meta name="citation_author" content="Barth, Mary E.">
#     <meta name="citation_title" content="Financial Accounting Research, Practice, and Financial Accountability">
#     <meta name="citation_online_date" content="2015/05/26">
# 
# This makes it easy to extract the content using Regular Expressions!

# In[35]:

re.findall(r'<meta name="citation_author" content="(.*)">', html_text)[0]


# In[36]:

re.findall(r'<meta name="citation_title" content="(.*)">', html_text)[0]


# In[37]:

re.findall(r'<meta name="citation_online_date" content="(.*)">', html_text)[0]


# ### Create a function that will extract everything when given an URL

# Writing a loop that contains all these `re.findall()` statements gets messy really fast.  
# A better solution is to write a function and call the function in the loop.

# In[38]:

def unpack_list(list_in, authors=False):
    if len(list_in) == 0: # Check whether the list is empty
        return ''
    elif authors:
        return list_in # We always want the authors variable to be a list
    else:
        return list_in[0] # If only 1 item and not authors: return single item


# Calling an index on a list (e.g. `list[0]`) will return an error if the list is empty.  
# This function above deals with this problem by including several conditions.

# In[39]:

def extract_info(url):
    html_text = urllib.request.urlopen(url).read().decode('utf-8')
    authors = unpack_list(re.findall(r'<meta name="citation_author" content="(.*)">', html_text), authors=True)
    title = unpack_list(re.findall(r'<meta name="citation_title" content="(.*)">', html_text))
    date = unpack_list(re.findall(r'<meta name="citation_online_date" content="(.*)">', html_text))
    return(title, authors, date)


# **Note: if you use Python 3 you need to use:**
# ```
# html_text = urllib.request.urlopen(url).read().decode('utf-8')
# ```

# We can call this function with any URL and it will return a `tuple` with the information.  
# A `tuple` is similar to a `list` but it is not mutable. 

# In[40]:

extract_info(ssrn_url['SSRN-id2610429.pdf'])


# ### Loop through all the PDF files

# We will loop through all the items in the `ssrn_url` dictionary.  
# **Note:**  
# SSRN will block our connection if we loop too fast. 
# To deal with this problem we include two things:
# 
# 1. We use `try` and `except` to catch any errors when SSRN blocks the connection.
# 2. If it fails we use `time.sleep(5)` so that Python will wait for 5 seconds.  
# 
# **Note: use `.items()` instead of `.items()` if you use Python 3**

# In[41]:

ssrn_details = {k : None for k, v in ssrn_url.items()}
for k, v in ssrn_url.items():
    while ssrn_details[k] == None:
        try:
            ssrn_details[k] = extract_info(v)
        except:
            print('Failed: ' + ssrn_ID[k])
            time.sleep(5)
            pass


# **Note:**
# I have saved the results to a file in case the above takes too long to run.  
# Load it using:  
# ```
# ssrn_details = pickle.load(open("ssrn_backup.p", "rb"))
# ```
# 
# In case you are interested, you can save dictionaries using:  
# ```
# pickle.dump(ssrn_details, open("ssrn_backup.p", "wb"))
# ```

# In[42]:

ssrn_details['SSRN-id1786360.pdf']


# # categorize the ssrn downloads

# ### Drop invalid SSRN downloads

# It might happen that an ID is not found by SSRN, we would like to remove these.  

# In[43]:

ssrn_details_v2 = {}
for k, v in ssrn_details.items():
    if v[0] != '' and v[1] != '':
        ssrn_details_v2[k] = v


# In[44]:

len(ssrn_details.keys()) - len(ssrn_details_v2.keys())


# **Optional part:**  
# 
# The `if` statements above are not very descriptive because we use the tuple index.  
# A better approach is to use a `namedtuple()` from the `collections` module.

# In[45]:

ssrn_details_named = {}
for k, v in ssrn_details.items():
    named_tuple = collections.namedtuple('tuple', 'title authors date')
    ssrn_details_named[k] = named_tuple(*v)


# In[46]:

ssrn_details_named['SSRN-id1786360.pdf'].title


# In[47]:

ssrn_details_v3 = {}
for k, v in ssrn_details_named.items():
    if v.title != '' and v.authors != '':
        ssrn_details_v3[k] = v


# As you can see `v.title` is immediately descriptive whereas `v[0]` is not.

# ## Change filename and move to different folder

# ### Generate a more informative file name

# Let's make the filename more descriptive of the working paper by changing it to:  
# `names (year)`

# In[48]:

ssrn_names = {}
for k, v in ssrn_details_v2.items():
    name = ', '.join([re.findall('^(.*),', name)[0].strip() for name in v[1]]) + ' (' + v[2][:4] + ').pdf'
    ssrn_names[k] = name


# In[49]:

ssrn_names['SSRN-id1786360.pdf']


# ### Copy the SSRN files with the new name

# We can perform 'file explorer' tasks using the build-in `shutil` module.

# In[50]:

cat_folder = r'SSRN'


# In case the folder does not exist --> make it:

# In[51]:

if not os.path.exists(cat_folder):
    os.makedirs(cat_folder)


# In[52]:

for k, v in ssrn_names.items():
    current = os.path.join(downloads_path, k)
    destination = os.path.join(cat_folder, v)
    try:
        shutil.copy(current, destination)
    except Exception as e:
        print('Failed to copy %s' % v)
        print(e)
        pass


# ## Create an Excel file with all the details

# We now have a bunch of dictionaries with different pieces of information.  
# We can create on multi-level dictionary that contains everthing but using the `pandas` package is easier.

# ### Convert all the dictionaries into a Pandas dataframe

# First we convert the `ssrn_names` dictionary into a Pandas dataframe.

# In[53]:

ssrn_dataframe = pd.DataFrame.from_dict(ssrn_names, orient='index')


# In[54]:

ssrn_dataframe.columns = ['new_name']


# In[55]:

ssrn_dataframe.head()


# Next we add the details from `ssrn_ctime`, `ssrn_url`, and `ssrn_details_v2`

# In[56]:

ssrn_dataframe['ctime'] = [time.ctime(ssrn_ctime[i]) for i in ssrn_dataframe.index]
ssrn_dataframe['title'] = [ssrn_details_v2[i][0] for i in ssrn_dataframe.index]
ssrn_dataframe['authors'] = [ssrn_details_v2[i][1] for i in ssrn_dataframe.index]
ssrn_dataframe['ssrn_date'] = [ssrn_details_v2[i][2] for i in ssrn_dataframe.index]
ssrn_dataframe['url'] = [ssrn_url[i] for i in ssrn_dataframe.index]


# In[57]:

ssrn_dataframe.head()


# ### Save dataframe to a CSV file

# We can easily save the dataframe to Excel using `.to_csv()`  
# **Note:** One of the major improvements of Python 3 is improved support for unicode.  
# Python 2.7 often gives errors that relate to encoding, these can be very annoying to solve.

# In[58]:

ssrn_dataframe.to_csv('ssrn_index.csv')

