
# coding: utf-8

# ## Variables

# In[20]:

a = 5
b = 'A string'


# ## Numbers

# In[21]:

2+2


# In[22]:

3 / 4


# *Note:* in Python 2.7 you need to do:

# In[23]:

3 / float(4)


# ## Strings

# Specify with single, double or tipple quotes

# In[24]:

hello = 'world'
saying = 'hello world'
paragraph = """ This is
a paragraph
"""


# ### Variables in strings

# In[25]:

'%d' % 20


# In[26]:

'%.3f %.2f' % (20, 1/3)


# *Note:* An alternative is to use `.format()`

# In[27]:

'{:.3f} {:.2f}'.format(20, 1/3)


# ## Lists, tuples and dictionaries

# ### Lists

# In[28]:

pets = ['dogs', 'cat', 'bird']
pets.append('lizard')
pets


# ### Tuple

# *Note:* You cannot add or remove elements from a tuple

# In[29]:

pets = ('dogs', 'cat', 'bird')
pets


# ### Dictionaries

# Unordered key, value pairs

# In[30]:

person = {'name': 'fred', 'age': 29}
person['age']


# In[31]:

person['money'] = 50
del person['age']
person


# ### Combinations

# In[32]:

mix = {'fruit' : [('apple', 'orange'), ('banana', 'pear')]}
mix['fruit'][0][1]


# ## Slicing

# If an object is ordered (such as a list) you can select on index  
# pets = ['dogs', 'cat', 'bird', 'lizzard']

# In[33]:

favorite_pet = pets[0]
favorite_pet


# In[34]:

reptile = pets[-1]
reptile


# In[35]:

pets[1:3]


# In[36]:

pets[:2]


# *Note:* this also works on strings:

# In[37]:

fruit = 'banana'
fruit[:2]


# ## Functions

# In[38]:

def add_5(number):
    return number + 5


# *Note:* the action of defining a function does not execute the code!  
# The code wil execute once you call the function:

# In[39]:

add_5(10)


# *Note:* You can add default values:

# In[40]:

def add(number, add=5):
    return number + add


# In[41]:

add(10)


# In[42]:

add(10, add=3)


# ## Display something

# In[43]:

print('Hello')


# In[44]:

print('Hello ' + 'World')


# In[45]:

print('I have', 2, 'apples')


# In[46]:

apples = 5
print('I have', apples, 'apples')


# ## Whitespace (blocks)

# Indentations are required by Python to sub-set blocks of code.  
# *Note:* these subsets have their own local scope, notice variable `a`:

# In[47]:

def example():
    a = 'Layer 1'
    print(a)
    
    def layer_2():
        a = 'Layer 2'
        print(a)
        
    layer_2()


# In[48]:

example()


# ## Conditionals

# In[49]:

grade = 95
if grade > 90:
    print('A')
elif grade > 80:
    print('B')
else:
    print('C')


# ## Looping

# In[50]:

count = 0
while count < 4:
    print(count)
    count += 1


# In[51]:

for num in range(0, 6, 2):
    print(num)


# In[52]:

list_fruit = ['Apple', 'Banana', 'Orange']
for fruit in list_fruit:
    print(fruit)


# In[53]:

for num in range(100):
    print(num)
    if num == 2:
        break


# Looping over a dictionary  
# *Note:* if using Python 2.7 you need to use `.iteritems()`

# In[54]:

dictionary = {'one' : 1, 'two' : 2, 'three' : 3}
for k, v in dictionary.items():
    print(k, v + 10)


# ## Comprehensions:

# A comprehension makes it easier to generate a list or dictionary using a loop.  
# *List comprehension:*

# In[55]:

new_list = [(x + 5) / 2 for x in range(0,6)]
new_list


# *Traditional way:*

# In[56]:

new_list = []
for x in range(0,6):
    new_list.append((x + 5) / 2)
new_list


# *Dictionary comprehension:*

# In[57]:

new_dict = {x : (x + 5) / 2 for x in range(0,6)}
new_dict


# *Traditional way:*

# In[58]:

new_dict = {}
for x in range(0,6):
    new_dict[x] = (x + 5) / 2
new_dict


# ## Catching Exceptions

# In[59]:

num_list = [1, 2, 3]


# In[62]:

num_list.remove(4)


# In[63]:

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

# In[64]:

import math
math.sin(1)


# In[65]:

import math as math_lib
math_lib.sin(1)


# In[66]:

from math import sin
sin(1)


# ## OS operations

# In[67]:

import os


# ### Get current working directory

# In[68]:

os.getcwd()


# ### List files/folders in directory

# In[69]:

os.listdir()


# ### Change working directory

# In[70]:

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

# In[71]:

with open('new_file.txt', 'w') as file:
    file.write('Content of new file. \nHi there!')


# In[72]:

with open('new_file.txt', 'r') as file:
    file_content = file.read()


# In[73]:

file_content


# In[74]:

print(file_content)


# In[75]:

with open('new_file.txt', 'a+') as file:
    file.write('\n' + 'New line')


# In[76]:

with open('new_file.txt', 'r') as file:
    print(file.read())


# *Note:* using `with` is best as it automatically closes the file
