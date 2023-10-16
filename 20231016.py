#!/usr/bin/env python
# coding: utf-8

# In[1]:


5%2


# In[2]:


5//2


# In[3]:


82+127


# In[4]:


25*24


# In[5]:


a = 2
if a != 1:
    print("1이 아님")


# In[6]:


a = 2
a = a * 10
a *= 10


# In[7]:


x = True
y = False

if x and y:
    print("Yes")
else:
    print("No")


# In[8]:


a = [1,2,3,4]
b = 3 in a
print(b)


# In[9]:


a = "ABC"
b = a
print(a is b)


# In[10]:


s = '가나다'
s = "가나다"
print(s)


# In[11]:


s = '''아리랑
아리랑
아라리요
'''
print(s)


# In[12]:


s = '''아리랑\n아리랑\n아라리요'''
print(s)


# In[13]:


p = "이름: %s 나이: %d" % ("김유신", 65)
print(p)


# In[14]:


p = "X = %0.3f, Y = %10.2f" % (3.141592, 3.141592)
print(p)


# In[15]:


s = "ABC"
type(s)
v = s[1]
print(v)
type(s[1])


# In[16]:


s = ','.join(['가나','다라','마바'])
print(s)


# In[17]:


s = ''.join(['가나','다라','마바'])
print(s)


# In[18]:


items = '가나,다라,마바'.split(',')
print(items)


# In[19]:


departure, _, arrivial = "Canada-Japan".partition('-')
print(departure)
#분리할 때는 .partition ('-') 구분 단위를 -로 함


# In[20]:


#위치를 기준으로 한 포맷팅
s = "Name: {0}, Age: {1}". format("임청아", 24)
print(s)


# In[21]:


# 필드명을 기준으로 한 포맷팅
s = "Name: {name}, Age: {age}". format(name = "임청아", age = 24)
print(s)


# In[22]:


# object의 인덱스 혹은 키를 사용하여 포맷팅
area = (10, 20)
s = "width: {x[0]}, height: {x[1]}".format(x = area)
print(s)


# In[23]:


print('Hello, world!')


# In[24]:


print('Hello'); print('1234')


# In[25]:


if x < 10:
    print(x)
    print("한자리수")


# In[26]:


if x < 100: print(x)


# In[ ]:




