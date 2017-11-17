
# coding: utf-8

# In[96]:


import numpy as np
import sys


# In[97]:


data = np.loadtxt(sys.argv[1])


# In[98]:


def sort_the_array(data, col):
    try:
        data = np.sort(data[:, col])[::-1]
        return data
    except:
        return None


# In[99]:


result = sort_the_array(data, int(sys.argv[2]))


# In[108]:


np.savetxt("ans1.txt", result, fmt='%.3f')

