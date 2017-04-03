
# coding: utf-8

# In[52]:

'''
A Dataframe as something with rows and columns. It is
similar to a spreadsheet, a database table, or R's data.frame object
'''
import pandas as pd
import numpy as np


# In[2]:

from numpy.random import randn
np.random.seed(101)


# In[5]:

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'],['W', 'X', 'Y', 'Z'])


# In[6]:

df #a dataframe is a bunch of series that share the same index


# In[7]:

df['W']


# In[8]:

type(df['W'])


# In[9]:

df.W #can access a column a la SQL; it reco that you use bracket notation


# In[11]:

df[['W','Z']]


# In[13]:

df['W']['A']


# In[21]:

df['AA'] = df['W'] + df['Y']
print(df)


# In[17]:

df.drop('AA',axis=1) # Not inplace unless specified!


# In[22]:

df.drop('AA',axis=1,inplace=True)


# In[24]:

df.drop('E')


# In[25]:

df.shape #df is tuple!


# In[26]:

df.loc['C'] #rows are also series


# In[27]:

df.iloc[2] #numerical based index selection


# In[28]:

# Selecting a subset of [rows, columns]
df.loc['B','Y']


# In[30]:

df.loc[['B','C'],['X','Z']]


# In[31]:

#conditional selection
df > 0


# In[32]:

#display values that are > 0 in the df
df[df>0]


# In[35]:

df['W'] > 0


# In[36]:

#filter a subset of rows where condition is true
df[df['W'] > 0]


# In[37]:

df[df['Z'] < 0]


# In[40]:

#select two clmns where condition is true
df[df['W']>0][['Y','Z']]


# In[44]:

# two or more conditions we can use '|' or '&' with parens
df[(df['W']>0) & (df['X'] > 1)]


# In[45]:

# Reset to default 0,1...n index
df.reset_index()


# In[46]:

df #does not happen inplace!


# In[48]:

newindex = 'CA NY WY OR CO'.split() #quick way to create a list


# In[49]:

df['States'] = newindex


# In[50]:

df


# In[51]:

df.set_index('States')


# In[53]:

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

