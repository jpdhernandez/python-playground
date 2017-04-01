
# coding: utf-8

# In[1]:

my_list = [1,2,3]


# In[2]:

import numpy as np


# In[4]:

arr = np.array(my_list)


# In[5]:

arr


# In[6]:

my_mat = [[1,2,3],[4,5,6],[7,8,9]]


# In[7]:

np.array(my_mat)


# In[9]:

np.arange(0,11,2)


# In[10]:

np.zeros(3)


# In[12]:

np.zeros((2,4))


# In[13]:

np.ones((3,4))


# In[28]:

np.linspace(0,20,20)


# In[15]:

np.eye(4) #identity matrix, a 2-dim square matrix


# In[29]:

np.random.rand(5)


# In[32]:

np.random.randn(4,4)


# In[35]:

np.random.randint(1,100,10)


# In[36]:

arr = np.arange(25)


# In[38]:

ranarr = np.random.randint(0,50,10)


# In[39]:

arr.reshape(5,5)


# In[40]:

ranarr.max()


# In[41]:

ranarr.min()


# In[42]:

ranarr.argmax()


# In[43]:

ranarr.argmin()


# In[44]:

arr = arr.reshape(5,5)


# In[46]:

arr.shape


# In[48]:

arr.dtype


# In[49]:

from numpy.random import randint


# In[50]:

randint(0,49)

