#!/usr/bin/env python
# coding: utf-8

# In[1]:


#reverse string
a= input("enter your String : ")
str = ''
for i in a:
    str = i + str
print("The Reversed String is: ", str)


# In[8]:


a=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("even number is",even)
print("odd number is",odd)

