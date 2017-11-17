
# coding: utf-8

# In[8]:


from PIL import Image
import sys


# In[9]:


im = Image.open(sys.argv[1])
im.rotate(180).save('ans2.png')

