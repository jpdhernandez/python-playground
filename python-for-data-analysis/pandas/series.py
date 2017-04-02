
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[4]:

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}


# In[5]:

pd.Series(data = my_data)


# In[7]:

pd.Series(my_data,labels)


# In[9]:

pd.Series(arr, labels) #np arrays work the same way as lists


# In[10]:

pd.Series(d)


# In[11]:

pd.Series(labels) #A series can hold any kind of data object in py


# In[12]:

pd.Series([sum, print, len]) #functions!


# In[16]:

#Series allows for fast look ups like a hash table or dictionary
series1 = pd.Series([1,2,3,4],['USA', 'Germany','USSR', 'Japan'])


# In[17]:

series1


# In[20]:

series2 = pd.Series([1,2,5,4],['USA', 'Germany','Italy', 'Japan'])


# In[19]:

series2


# In[22]:

series1['USA']


# In[24]:

series3 = pd.Series(labels)


# In[25]:

series3


# In[26]:

series3[2]


# In[29]:

#operations are matched based off of index, ints will be coverted to floats
series1 + series2


# In[32]:

series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
print(series)


# In[34]:

'''
You can also manually assign indices to the items in the Series when
creating the series
'''
series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                    ['Instructor', 'Curriculum Manager',
                     'Course Number', 'Power Level'])
print(series)


# In[38]:

#You can use index to select specific items from the Series
series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                    ['Instructor', 'Curriculum Manager',
                    'Course Number', 'Power Level'])
print(series['Instructor'])
print("---------")
print(series[['Instructor', 'Curriculum Manager', 'Course Number']])


# In[40]:

#You can also use boolean operators to select specific items from the Series
cuteness = pd.Series([1, 2, 3, 4, 5],
                     ['Cockroach', 'Fish',
                      'Mini Pig','Puppy', 'Kitten'])
print(cuteness > 3)
print("---------")
print(cuteness[cuteness > 3])

