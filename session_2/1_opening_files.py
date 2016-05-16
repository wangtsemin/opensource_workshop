
# coding: utf-8

# # python hands-on session

# By: Ties de Kok  
# Version: Python 2.7 (see any notes for Python 3.5)

# 1. **handling files**
# 2. data handling
# 3. web scraping
# 4. text mining
# 5. (interactive) visualisations

# ## Introduction

# It is possible to open and save a wide variety of file formats using Python.  
# There are often multiple ways to open a particular file format, the examples below are what I like to use. 

# ## Indexing a folder

# In many instances you want to loop over all the files in a folder.  
# There are multiple ways to go about this but I like to use:

# In[1]:

import os


# ### If the folder contains only files:

# In[23]:

folder = r'C:\Stack\Work\Workshops\python_workshop'
filenames = os.listdir(folder)
filepaths = [os.path.join(folder, name) for name in filenames]


# ### Files are in multiple sub-folders

# If the folder contains multiple levels we need to use a more advanced technique

# In[63]:

folder = r'C:\Stack\Work\Workshops\python_workshop'
filepaths = []
for root,dirs,files in os.walk(folder):
    for i in files:
        filepaths.append(os.path.join(root,i))


# ## Text files

# Opening text files is done using the default Python library.

# You can open a file with different file modes:  
# w -> write only  
# r -> read only  
# w+ -> read and write + completely overwrite file  
# a+ -> read and write + append at the bottom  

# ### Opening a file

# In[ ]:

with open(r'C:\file.txt', 'w+') as file:
    file_content = file.read()


# ### Writing to a file

# In[ ]:

with open(r'C:\file.txt', 'w+') as file:
    file.write('Content of new file. \nHi there!')


# ### Additional information

# Note that I am using a `with` statement when opening files.  
# Another method is to use `open` and `close`:

# In[ ]:

f = open(r'C:\file.txt', 'w+')
file_content = f.read()
f.close()


# The `with` method is prefered as it automatically closes the file.  
# This prevents the file from being 'in use' if you forget to use `.close()`

# ### Looping over indexed files

# In[ ]:

for i in filepaths:
    with open(i, 'w+') as f:
        file_content = f.read()


# ## Excel and .csv files

# There are many ways to open these files, I like to use `Pandas`

# In[65]:

import pandas as pd


# ### Open Excel file

# This function has a lot of options, see:  
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html  
# 
# *Note:* You often want to add `, encoding='utf-8'`

# In[ ]:

excel_file = pd.read_excel(r'C:\file.xls')


# ### Save Excel file

# This saves a `Pandas` dataframe object, see the data handling file.  
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html  
# 
# *Note:* You can save as `.xls` but also `.xlsx`

# In[ ]:

df = pd.DataFrame()
df.to_excel(r'C:\file.xls')


# ### Open CSV file

# There are many many ways to open a CSV file, I will show the Pandas function.  
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html

# In[ ]:

csv_file = pd.read_csv(r'C:\file.csv', sep=';')


# ### Save CSV file

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html

# In[ ]:

df = pd.DataFrame()
df.to_csv(r'C:\file.csv', sep=';')


# ## Stata and SAS files

# Pandas can also open and save Stata and open SAS files

# ### Stata

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_stata.html  
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_stata.html

# In[ ]:

stata_file = pd.read_stata(r'C:\file.dta')


# In[ ]:

df = pd.DataFrame()
df.to_stata(r'C:\file.dta')


# *Note: make sure you have the latest version of Pandas for new Stata versions*

# ### SAS

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sas.html  
# This function works in most cases but files with text can throw nasty encoding errors.

# In[ ]:

sas_file = pd.read_sas(r'C:\file.sas7bdat', format='sas7bdat')


# ## JSON files

# ### Convert JSON file to Pandas dataframe

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_json.html  
# 
# *Note:* The path can also be a url

# In[ ]:

json_df = pd.read_json(r'C:\file.json')


# ### Use the `json` module

# In[ ]:

import json


# **Read:**

# In[ ]:

with open(r'C:\file.json', 'r') as f:
    json_data = json.load(f)


# **Write:**

# In[ ]:

data = {
   'name' : 'Ties',
   'location' : 'Tilburg',
}

with open(r'C:\file.json', 'w') as f:
    json.dump(data, f)


# ## HDF files

# You often run into the problem of having to store large amounts of data.  
# The traditional formats such as .csv are not very efficient as big-data file formats.  
# 
# I like to use the `Hierarchical Data Format` or `HDF` in short.
# This `.hdf` file format is designed to store and organize large amounts of data. 
# 
# Writing and reading `.hdf` files is extremely fast compared to `.csv`:
# 
# **Writing:**
# 
# ```
# %timeit test_hdf_fixed_write(df)
# 1 loops, best of 3: 237 ms per loop
# 
# %timeit test_hdf_table_write(df)
# 1 loops, best of 3: 901 ms per loop
# 
# %timeit test_csv_write(df)
# 1 loops, best of 3: 3.44 s per loop
# ```
# 
# **Reading:**
# 
# ```
# %timeit test_hdf_fixed_read()
# 10 loops, best of 3: 19.1 ms per loop
# 
# %timeit test_hdf_table_read()
# 10 loops, best of 3: 39 ms per loop
# 
# %timeit test_csv_read()
# 1 loops, best of 3: 620 ms per loop
# ```

# ### Read and write HDF files using Pandas

# This is used to read and write Pandas dataframes  
# 
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_hdf.html  
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_hdf.html
# 
# *Note*: You can give it any `key` you like. I always use the filename with `.h5` as `key`

# In[ ]:

hdf_df = pd.read_hdf(r'C:\file.h5', 'file') # Second argument is the key


# In[ ]:

df = pd.DataFrame()
df.to_hdf(r'C:\file.h5', 'file')


# ### Using HDF with big data that does not fit into memory

# One big advantage of `HDF` is that it does not require all the data to be load into memory at once. 
# 
# See the page below for a very comprehensive overview:  
# http://pandas.pydata.org/pandas-docs/stable/io.html#io-hdf5
