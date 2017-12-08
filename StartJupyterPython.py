
# coding: utf-8

# Test code

# In[17]:

print("Hello World")


# In[18]:

name = "jon"


# In[19]:

name


# In[23]:

get_ipython().system('pip list')


# In[25]:

get_ipython().magic('lsmagic')


# In[26]:

get_ipython().magic('pwd')


# In[27]:

get_ipython().magic('ls')


# In[29]:

get_ipython().magic('ls -la')


# In[32]:

get_ipython().magic('matplotlib inline')


# In[34]:

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


# In[35]:

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# In[54]:

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(5,3)), columns=list('ABC'))


# In[55]:

df


# In[ ]:



