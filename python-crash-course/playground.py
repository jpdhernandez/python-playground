
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


# In[12]:

5 % 2


# In[13]:

var = 2


# In[14]:

var


# In[15]:

x = 2


# In[16]:

y = 3


# In[17]:

x + y


# In[18]:

x = x + x


# In[19]:

x


# In[20]:

name_of_var = 12


# In[21]:

# Strings


# In[22]:

'single quote'


# In[23]:

"another string"


# In[24]:

"I can't go"


# In[25]:

x = "hello"


# In[26]:

x


# In[27]:

print(x)


# In[28]:

num = 12
name = "Sam"


# In[29]:

print('My number is {} and my name is {}, more {}'.format(num, name, num))


# In[30]:

print('My number is {one} and my name is {two}, more {one}'.format(one=num,two=name))


# In[31]:

s = "hello"


# In[32]:

s[0]


# In[33]:

s[4]


# In[34]:

z = "abcdefghijklmn"


# In[35]:

z[0:3]


# In[36]:

z[3:]


# In[37]:

z[:6]


# In[38]:

z[3:6]


# In[39]:

[1,2,3]


# In[40]:

["a","b", "c"]


# In[41]:

my_list = ["a","b", "c"]


# In[42]:

my_list.append("d")


# In[43]:

my_list


# In[44]:

my_list[0]


# In[45]:

my_list[1:3]


# In[46]:

my_list[0] = "NEW"


# In[47]:

my_list


# In[48]:

nest =  [1,2,[3,4]]


# In[49]:

nest


# In[50]:

nest[2]


# In[51]:

nest[2][1]


# In[52]:

nest = [1,2,[3,4,["getThis"]]]


# In[53]:

nest


# In[54]:

print(nest[2][2])


# In[55]:

dictionary = {"key":"value","key1":"value1"}


# In[56]:

dictionary


# In[57]:

d = dictionary


# In[58]:

d["key"]


# In[59]:

d = {"k1":[1,2,3]}


# In[60]:

d["k1"][1]


# In[61]:

d = {"k": {"nestedKey":[1,2]}}


# In[62]:

d["k"]["nestedKey"][0]


# In[63]:

True


# In[64]:

False


# In[65]:

tupple = (1,2,3)


# In[66]:

tupple[2]


# In[67]:

t = tupple


# In[68]:

t[0] = 1 #immutable 


# In[69]:

{1,1,1,2,2,2,3,3,3,}


# In[70]:

set({1,1,1,2,2,2,3,3,3})


# In[71]:

s = {1,2,3}


# In[72]:

s.add(5)


# In[73]:

s


# In[74]:

s.add(5)


# In[75]:

s


# In[76]:

1 > 2


# In[77]:

1 < 2


# In[78]:

1 >= 2


# In[79]:

1 == 1


# In[80]:

1 == 2


# In[81]:

1 != 3


# In[82]:

"hi" == "hi"


# In[83]:

1 < 2 and 2 < 3


# In[84]:

1 < 1 and 2 > 3


# In[85]:

1 < 2 or 2 > 3


# In[86]:

if 1 < 2:
    print("yep!")


# In[87]:

if 1 == 2:
    print("first")
elif 3 == 3:
    print ("second")
else:
    print("last")


# In[88]:

seq = [1,2,3,4,5]


# In[89]:

for  item in seq:
    print(item)


# In[91]:

i = 1
while i <= 5:
    print("i is {}".format(i))
    i = i + 1


# In[93]:

list(range(10))


# In[94]:

x = [1,2,3,4]


# In[95]:

out = []
for num in x:
    out.append(num**2)
print(out)


# In[96]:

#list comprehension
[num**2 for num in x]


# In[105]:

def fn(name='default'):
    print("Hello " +  name)


# In[104]:

fn("Julian")


# In[108]:

fn()


# In[112]:

def sq(num):
    """
    This is a docstring
    A multi line comment
    this fn squares a num
    """
    return num**2


# In[110]:

o = sq(2)


# In[111]:

o

