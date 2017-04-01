
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

arr = np.arange(0,11)


# In[3]:

arr


# In[4]:

arr[8]


# In[5]:

arr[1:5]


# In[6]:

arr[:6]


# In[7]:

arr[:5] = 99 #broadcast the value


# In[8]:

arr


# In[9]:

arr = np.arange(0,11)


# In[11]:

slice_of_arr = arr[0:6] #reference to the first five elements


# In[17]:

arr_copy = arr.copy() #shallow copy


# In[14]:

arr_copy[:] = 100


# In[15]:

print(arr_copy)


# In[16]:

print(arr)


# In[19]:

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])


# In[22]:

arr_2d


# In[26]:

arr_2d[1,2] #index slicing


# In[28]:

arr_2d[:2,1:]


# In[29]:

arr_2d[1:]


# In[31]:

bool_arr = arr > 4 #conditional selection


# In[32]:

bool_arr


# In[33]:

arr[bool_arr]


# In[34]:

arr[arr>5]


# In[35]:

arr_2d = np.arange(50).reshape(5,10)


# In[36]:

arr_2d #index slicing practice


# In[38]:

arr_2d[1:3,3:5]

