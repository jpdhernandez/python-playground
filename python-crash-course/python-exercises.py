
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:

7**4


# ** Split this string:**
# 
#     s = "Hi there Julian!"
#     
# **into a list. **

# In[7]:

s = "Hi there Julian!"


# In[8]:

s.split(" ")


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[9]:

planet = "Earth"
diameter = 12742


# In[13]:

print('The diameter of {} is {} kilometers.'.format(planet, diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[15]:

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[18]:

print(lst[3][1][2][0])


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[22]:

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[27]:

d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[23]:

# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[30]:

def domainGet(dm):
    return dm.split("@")[1]


# In[31]:

domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[41]:

def findDog(str):
    str = str.lower()
    return str.find('dog') != 0


# In[42]:

findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[44]:

def countDog(str):
    return str.lower().count('dog')


# In[45]:

countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[47]:

seq = ['soup','dog','salad','cat','great']


# In[48]:

list(filter(lambda sq:sq[0] == 's', seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[53]:

def caught_speeding(speed, is_birthday):
    if speed <= 60 or (speed <= 65 and is_birthday):
        return 'No ticket'
    elif speed >= 61 and speed <= 80 or (speed >= 66 and speed <= 85 and is_birthday):
        return 'Small ticket'
    elif speed >= 81:
        return "Big Ticket"


# In[56]:

caught_speeding(85,True)


# In[57]:

caught_speeding(81,False)