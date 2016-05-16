
# coding: utf-8

# # python hands-on session

# By: Ties de Kok  
# Version: Python 2.7 (see any notes for Python 3.5)

# 1. handling files
# 2. **data handling**
# 3. web scraping
# 4. text mining
# 5. (interactive) visualisations

# ## Introduction

# For the data handling part we will be using Python + Pandas.  
# What is `Pandas`?
# 
# > pandas is an open source, BSD-licensed library providing high-performance, easy-to-use  data structures and data analysis tools for the Python programming language.
# 
# In other words, whenever you want to use a datastructure with rows and columns, use `Pandas`!
# 
# A Pandas data object is called a `dataframe`.
# 
# 

# ## Format of this notebook

# The `Pandas` library is massive, it includes an enormous amount of functionality.  
# It is, therefore, impossible to cover everything in this notebook.  
# 
# PyCon 2015 (A Python conference) included a tutorial/talk by Brandon Rhodes.  
# This entire talk is available on YouTube and I think it is really great:  
# https://www.youtube.com/watch?v=5JnMutdy6Fw
# 
# I will build on his materials and add some tips of my own, but I highly recommend to also watch the video.
# 
# The full materials of Brandon's Pandas Tutorial are available here:  
# https://github.com/brandon-rhodes/pycon-pandas-tutorial

# # Some tips and tricks

# ## Import Pandas

# In[87]:

import pandas as pd
import numpy as np


# ## Create a dataframe

# ### Load file into Pandas

# To open a data file such as Excel, CSV, Stata, SAS, HDF see the first notebook.

# In[107]:

df_auto = pd.read_csv(r'auto_df.csv', sep=';', index_col='Unnamed: 0')


# **Create new dataframe from scratch**  
# We can create a new dataframe and pass data to it:

# In[88]:

d = {'col1': [1,2,3,4], 'col2': [5,6,7,8]}
df = pd.DataFrame(data=d)
df


# **Create dataframe from a dictionary**  
# We can also directly convert a dictionary to a dataframe:

# In[89]:

d = {'row1': [1,2,3,4], 'row2': [5,6,7,8]}
df = pd.DataFrame.from_dict(d, orient='index')
df


# ## Rename columns

# We can either manipulate `df.columns` directly or use `df.rename()`

# In[90]:

df.columns = ['col1', 'col2', 'col3', 'col4']
df


# In[91]:

df.rename(columns={'col1' : 'column1', 'col2' : 'column2'})


# **Note:** The above creates a copy, it does not modify it in place!  
# We need to use either the `inplace=True` argument or assign it:

# In[92]:

df = df.rename(columns={'col1' : 'column1', 'col2' : 'column2'})
#or
df.rename(columns={'col1' : 'column1', 'col2' : 'column2'}, inplace=True)


# ## Manipulate dataframe

# ### Add column

# In[93]:

df['col5'] = [10, 10]
df


# ### Add row

# In[94]:

df.loc['row3'] = [11, 12, 13, 14, 15]
df


# ### Inverse the dataframe

# In[95]:

df.T


# ### Remove column

# In[96]:

df = df.drop('col5', axis=1)
df


# ### Remove row

# In[97]:

df = df.drop('row1', axis=0)
df


# ### Set index

# In[121]:

df.set_index('column1')


# *Note:* `Pandas` also allows a multi-index. These can be very powerful. 

# In[122]:

df.set_index('column1', append=True)


# ## Select parts of the dataframe

# ### View entire dataframe

# Programs like Stata, SAS, and Excel include a data viewer.  
# Python and Pandas does not, it is therefore helpful to be able to quickly generate a view that you like. 

# In[108]:

df_auto


# ### Get top or bottom of dataframe

# In[109]:

df_auto.head(3)


# In[110]:

df_auto.tail(3)


# ### Select columns based on name

# *Note:* If you want multiple columns you need to use double brackets.

# In[112]:

df_auto[['make', 'price', 'mpg']].head(10)


# ### Select columns based on position

# *Note:* In the example below the first `0:5` selects the first 5 rows.

# In[220]:

df_auto.iloc[0:5, 2:5]


# ### Select based on index value

# In[207]:

df = df_auto[['make', 'price', 'mpg', 'trunk', 'headroom']].set_index('make')


# In[208]:

df.loc['Buick Riviera']


# ### Select based on index position

# In[211]:

df.iloc[2:5]


# ### Select based on condition

# In[117]:

df_auto[ df_auto.price < 3800 ]


# In[118]:

df_auto[(df_auto.price < 3800) & (df_auto.foreign == 'Foreign')]


# **Note:** all the above return new dataframes that are removed if we do not assign them.  
# If we want to keep it as a separate dataframe we have to assign it like so:

# In[124]:

df_auto_small = df_auto[(df_auto.price < 3800) & (df_auto.foreign == 'Foreign')]
df_auto_small


# ### Sort dataframe

# In[140]:

df_auto.sort_values(by=['headroom', 'trunk'], inplace=True)
df_auto.head()


# ## Generate new columns from within a dataframe

# You often want to create a new column using values that are already in the dataframe. 

# ### Combine columns

# *Note:* You can select a column using:
# 1. `df_auto['price']`
# 2. `df_auto.price` --> but this one only works if there are no spaces in the column name

# In[128]:

df_auto['price_trunk_ratio'] = df_auto.price / df_auto.trunk
df_auto[['make', 'price', 'trunk', 'price_trunk_ratio']].head()


# ### Generate a column by iterating over the rows

# There are many different ways to iterate over rows.  
# They mainly different in their trade-off between ease-of-use and performance.  
# 
# I will demonstrate the methods I like to use, the example goal:  
# > If the car is a foreign brand, multiple the price by 1.5

# **Using a list comprehension:**

# In[143]:

df_auto['new_price'] = [p*1.5 if f == 'Foreign' else p for p, f in zip(df_auto.price, df_auto.foreign)]
df_auto[['make', 'price', 'foreign', 'new_price']].head()


# **Using `.apply()`**

# *Note:* `lambda` is a so-called anonymous function.

# In[152]:

df_auto['new_price'] = df_auto.apply(lambda x: x.price*1.5 if x.foreign == 'Foreign' else x.price, axis=1)
df_auto[['make', 'price', 'foreign', 'new_price']].head()


# **Using `.apply()` with a function**

# In the example above we use an anonymous `lambda` function.  
# For more complex processing it is possible to use a defined function and call it in `.apply()`  
# 
# **Personal note:** This method is in my opinion prefered as it is a lot easier to read.

# In[153]:

def new_price_function(x):
    if x.foreign == 'Foreign':
        return x.price * 1.5
    else:
        return x.price


# In[155]:

df_auto['new_price'] = df_auto.apply(new_price_function, axis=1)
df_auto[['make', 'price', 'foreign', 'new_price']].head()


# ## Group-by operations

# Pandas `.groupby()` allows us to:  
# 1. Compute a summary statistic about each group
# 2. Perform some group-specific computations
# 3. Filter based on groups
# 
# See: http://pandas.pydata.org/pandas-docs/stable/groupby.html

# ### Create a group object:

# In[173]:

col_list = ['price', 'mpg', 'headroom', 'trunk', 'weight', 'length']
grouped = df_auto[col_list + ['foreign']].groupby(['foreign'])


# ### Compute mean summary statistic:

# In[174]:

grouped.mean()


# ### Retrieve particular group:

# In[180]:

grouped.get_group('Domestic').head()


# ### Group specific iteration

# In[178]:

for name, group in grouped:
    print(name)
    print(group.head())


# ## Combining dataframes

# In[195]:

df_auto_p1 = df_auto[['make', 'price', 'mpg']]
df_auto_p2 = df_auto[['make', 'headroom', 'trunk']]


# In[188]:

df_auto_p1.head(3)


# In[189]:

df_auto_p2.head(3)


# ### Merge datasets

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html

# In[192]:

merged_auto = pd.merge(df_auto_p1, df_auto_p2, how='left', on='make')
merged_auto.head(3)


# ### Join datasets on index

# In[196]:

df_auto_p1.set_index('make', inplace=True)
df_auto_p2.set_index('make', inplace=True)


# In[200]:

joined_auto = df_auto_p1.join(df_auto_p2)
joined_auto.reset_index().head(3)


# ## Reshaping and Pivot Tables

# In[ ]:




# ## Handling missing values

# http://pandas.pydata.org/pandas-docs/stable/missing_data.html

# ### Add missing values

# *Note:* We define a missing value as `np.nan` for convenience

# In[250]:

df_auto.loc['UvT_Car'] = [np.nan for x in range(0,len(df_auto.columns))]
df_auto.loc['UvT_Bike'] = [np.nan for x in range(0,len(df_auto.columns))]


# In[253]:

df_auto.loc[['UvT_Car', 'UvT_Bike']]


# ### Condition based on missing values

# Always use `pd.isnull()` or `pd.notnull()` as it is most reliable.  
# `df_auto.make == np.nan` will sometimes work but not always!

# In[254]:

df_auto[pd.isnull(df_auto.make)]


# In[255]:

df_auto[pd.notnull(df_auto.make)].head()


# ### Filling missing values

# To fill missing values with something we can use `.fillna()`

# In[257]:

df = df_auto.fillna('Missing')
df.loc[['UvT_Car', 'UvT_Bike']]


# ### Drop axis with missing values

# To drop missing values we can use `.dropna()`

# In[271]:

df_auto['make'].tail(3)


# In[272]:

df = df_auto.dropna(axis=0)
df['make'].tail(3)


# ## Changing datatypes

# ### Show current datatypes:

# In[221]:

df_auto.dtypes


# ### Convert datatypes

# The official function is called `.astype()`  

# In[244]:

df_auto['length'] = df_auto['length'].astype('str')
df_auto[['length']].dtypes


# In[243]:

df_auto['length'] = df_auto['length'].astype('int')
df_auto[['length']].dtypes


# ## Dates

# In[ ]:



