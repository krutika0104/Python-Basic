#!/usr/bin/env python
# coding: utf-8

# # 4. Accept three sides of triangle and check whether the triangle is possible or not.
# (triangle is possible only when sum of any two sides is greater than 3rd side)

# In[1]:


side1=int(input("Enter First Side:"))
side2=int(input("Enter Second Side:"))
side3=int(input("Enter Third Side:"))
if side1+side2>side3 or side2+side3>side1 or side3+side1>side2:
    print("The Sides Forms Triangle")
else:
    print("The Sides does not forms Triangle")

