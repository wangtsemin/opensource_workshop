
# coding: utf-8

# ## Variables

# In[1]:

a = 5
b = 'A string'


# ## Numbers

# In[2]:

2+2


# In[3]:

3 / 4


# *Note:* in Python 2.7 you need to do:

# In[4]:

3 / float(4)


# ## Strings

# Specify with single, double or tipple quotes

# In[5]:

hello = 'world'
saying = 'hello world'
paragraph = """ This is
a paragraph
"""


# ### Variables in strings

# In[6]:

'%d' % 20


# In[7]:

'%.3f %.2f' % (20, 1/3)


# ## Lists, tuples and dictionaries

# ### Lists

# In[8]:

pets = ['dogs', 'cat', 'bird']
pets.append('lizard')
pets


# ### Dictionaries

# Unordered key, value pairs

# In[9]:

person = {'name': 'fred', 'age': 29}
person['age']


# In[10]:

person['money'] = 50
del person['age']
person


# ## Slicing

# If an object is ordered (such as a list) you can select on index  
# pets = ['dogs', 'cat', 'bird', 'lizzard']

# In[11]:

favorite_pet = pets[0]
favorite_pet


# In[12]:

reptile = pets[-1]
reptile


# In[13]:

pets[1:3]


# In[14]:

pets[:2]


# In[15]:

fruit = 'banana'
fruit[:2]


# ## Functions

# In[16]:

def add_5(number):
    return number + 5

add_5(10)


# In[17]:

def add(number, add=5):
    return number + add


# In[18]:

add(10)


# In[19]:

add(10, add=3)


# ## Display something

# In[20]:

print('Hello')


# In[21]:

print('Hello ' + 'World')


# In[22]:

print('I have', 2, 'apples')


# In[23]:

apples = 5
print('I have', apples, 'apples')


# ## Whitespace (blocks)

# Indentations are required by Python to sub-set blocks of code

# In[24]:

def example():
    a = 'Layer 1'
    print(a)
    
    def layer_2():
        a = 'Layer 2'
        print(a)
        
    layer_2()


# In[25]:

example()


# ## Conditionals

# In[26]:

grade = 95
if grade > 90:
    print('A')
elif grade > 80:
    print('B')
else:
    print('C')


# ## Looping

# In[27]:

count = 0
while count < 4:
    print(count)
    count += 1


# In[28]:

for num in range(0, 6, 2):
    print(num)


# In[29]:

list_fruit = ['Apple', 'Banana', 'Orange']
for fruit in list_fruit:
    print(fruit)


# In[30]:

for num in range(100):
    print(num)
    if num == 2:
        break


# ## Catching Exceptions

# In[31]:

num_list = [1, 2, 3]


# In[32]:

num_list.remove(4)


# In[33]:

num_list = [1, 2, 3]
try:
    num_list.remove(4)
except ValueError as e:
    print('Number not in the list')
except Exception as e:
    print ('Generic error')
finally:
    print('Done')
    


# ## Importing Libraries

# In[34]:

import math
math.sin(1)


# In[35]:

import math as math_lib
math_lib.sin(1)


# In[36]:

from math import sin
sin(1)


# ## OS operations

# In[37]:

import os


# ### Get current working directory

# In[38]:

os.getcwd()


# ### List files/folders in directory

# In[39]:

os.listdir()


# ### Change working directory

# In[40]:

os.chdir(r'C:\Stack\Work\Workshops\python_workshop\opensource_workshop\cheat_sheet')


# *Note:* `r'path'` indicates a raw string  
# A raw string does not see `\` as a special character

# ## File Input/Output

# You can open a file with different file modes:  
# `w` -> write only  
# `r` -> read only  
# `w+` -> read and write + completely overwrite file   
# `a+` -> read and write + append at the bottom
# 

# In[41]:

with open('new_file.txt', 'w') as file:
    file.write('Content of new file. \nHi there!')


# In[42]:

with open('new_file.txt', 'r') as file:
    file_content = file.read()


# In[43]:

file_content


# In[44]:

print(file_content)


# In[45]:

with open('new_file.txt', 'a+') as file:
    file.write('\n' + 'New line')


# In[46]:

with open('new_file.txt', 'r') as file:
    print(file.read())


# *Note:* using `with` is best as it automatically closes the file
