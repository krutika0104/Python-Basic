#!/usr/bin/env python
# coding: utf-8

# 5. Check whether the given key is present in the dictionary or not
# 

# In[2]:


dict1={1:'krutika',2:'pink',3:'kalyan'}
key=int(input("Enter the key:"))
if key in dict1:
    print("The key is present")
else:
    print("The key is not present")

