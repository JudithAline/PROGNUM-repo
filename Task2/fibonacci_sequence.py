#!/usr/bin/env python
# coding: utf-8

# In[20]:


# the 2 starting values of the fibonnaci sequence
a = 1
b = 1
for f in range(49):    # 100-2 = 98 / 2 = 49 repeats of this
    a = a + b
    b = b + a

print("The 100th value of the fibonacci sequence is:", b)


# In[ ]:




