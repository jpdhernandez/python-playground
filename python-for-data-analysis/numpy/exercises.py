
# coding: utf-8

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:

import numpy as np


# #### Create an array of 10 zeros 

# In[3]:

np.zeros(10)


# #### Create an array of 10 ones

# In[4]:

np.ones(10)


# #### Create an array of 10 fives

# In[15]:

arr = np.zeros(10)
arr[:] = 5
arr
# or np.zeros(10) + 5 or ones * 5


# #### Create an array of the integers from 10 to 50

# In[16]:

np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[17]:

np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[29]:

arr = np.arange(0,9)
arr.reshape(3,3)


# #### Create a 3x3 identity matrix

# In[26]:

np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[35]:

np.random.randn(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[60]:

np.random.randn(25)


# #### Create the following matrix:

# In[45]:

np.linspace(0.01,1,100).reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[46]:

np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[47]:

mat = np.arange(1,26).reshape(5,5)
mat


# In[48]:

mat[2:,1:]


# In[49]:

mat[3,4]


# In[50]:

mat[0:3,1:2]


# In[51]:

mat[4]


# In[52]:

mat[3:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[54]:

mat.sum()


# #### Get the standard deviation of the values in mat

# In[56]:

mat.std()


# #### Get the sum of all the columns in mat

# In[61]:

mat.sum(axis=0) #[sum(mat[:,i]) for i in range(5)] 

