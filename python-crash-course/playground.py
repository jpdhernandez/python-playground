
# coding: utf-8

# In[1]:

1


# In[2]:

1.0


# In[3]:

1 + 1


# In[4]:

1 * 3


# In[5]:

1 / 3


# In[6]:

1 / 2.0


# In[7]:

1 / 2


# In[8]:

2 ** 4


# In[9]:

2 + 3 * 5 + 5


# In[10]:

(2 + 3) * (5 + 5)


# In[11]:

4 % 2


# In[13]:

5 % 2


# In[14]:

var = 2


# In[15]:

var


# In[16]:

x = 2


# In[17]:

y = 3


# In[19]:

x + y


# In[20]:

x = x + x


# In[21]:

x


# In[23]:

name_of_var = 12


# In[24]:

# Strings


# In[25]:

'single quote'


# In[26]:

"another string"


# In[27]:

"I can't go"


# In[28]:

x = "hello"


# In[29]:

x


# In[30]:

print(x)


# In[31]:

num = 12
name = "Sam"


# In[36]:

print('My number is {} and my name is {}, more {}'.format(num, name, num))


# In[35]:

print('My number is {one} and my name is {two}, more {one}'.format(one=num,two=name))


# In[37]:

s = "hello"


# In[38]:

s[0]


# In[39]:

s[4]


# In[40]:

z = "abcdefghijklmn"


# In[41]:

z[0:3]


# In[42]:

z[3:]


# In[43]:

z[:6]


# In[44]:

z[3:6]


# In[45]:

[1,2,3]


# In[46]:

["a","b", "c"]


# In[47]:

my_list = ["a","b", "c"]


# In[48]:

my_list.append("d")


# In[49]:

my_list


# In[50]:

my_list[0]


# In[51]:

my_list[1:3]


# In[52]:

my_list[0] = "NEW"


# In[53]:

my_list


# In[54]:

nest =  [1,2,[3,4]]


# In[55]:

nest


# In[56]:

nest[2]


# In[57]:

nest[2][1]


# In[58]:

nest = [1,2,[3,4,["getThis"]]]


# In[59]:

nest


# In[60]:

print(nest[2][2])


# In[61]:

dictionary = {"key":"value","key1":"value1"}


# In[63]:

dictionary


# In[64]:

d = dictionary


# In[67]:

d["key"]


# In[68]:

d = {"k1":[1,2,3]}


# In[69]:

d["k1"][1]


# In[70]:

d = {"k": {"nestedKey":[1,2]}}


# In[72]:

d["k"]["nestedKey"][0]


# In[73]:

True


# In[74]:

False


# In[75]:

tupple = (1,2,3)


# In[77]:

tupple[2]


# In[78]:

t = tupple


# In[79]:

t[0] = 1 #immutable 


# In[80]:

{1,1,1,2,2,2,3,3,3,}


# In[81]:

set({1,1,1,2,2,2,3,3,3})


# In[82]:

s = {1,2,3}


# In[83]:

s.add(5)


# In[84]:

s


# In[85]:

s.add(5)


# In[86]:

s


# In[87]:

1 > 2


# In[88]:

1 < 2


# In[89]:

1 >= 2


# In[90]:

1 == 1


# In[91]:

1 == 2


# In[92]:

1 != 3


# In[93]:

"hi" == "hi"


# In[94]:

1 < 2 and 2 < 3


# In[95]:

1 < 1 and 2 > 3


# In[96]:

1 < 2 or 2 > 3


# In[97]:

if 1 < 2:
    print("yep!")


# In[99]:

if 1 == 2:
    print("first")
elif 3 == 3:
    print ("second")
else:
    print("last")


# In[ ]:



