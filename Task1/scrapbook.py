#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sirius data
m = input(-1.46)
M = input(1.45)


# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164


# In[1]:


sun = 1.989e30
print(sun)


# In[2]:


x3 = "hallo"
print(x3)


# In[7]:


# Sirius data
m = float(input("apparentMagnitude:"))
M = float(input("absoluteMagnitude:"))

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

apparentMagnitude = m
absoluteMagnitude = M

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164

x = f"The distance to Sirius is: {d}"
print(x)


# In[ ]:




