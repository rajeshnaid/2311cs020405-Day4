#!/usr/bin/env python
# coding: utf-8

# In[3]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter+1
        sum +=x
    mean = sum/counter
    return mean


# In[5]:


def product(*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result


# In[27]:


product(1,2,3,4,5,6,7,8,9)


# In[ ]:




