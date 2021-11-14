#!/usr/bin/env python
# coding: utf-8

# In[44]:


import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed
from PIL import Image
from skimage import io
from skimage.transform import resize
url = 'https://i.imgur.com/9rKTgvo.png'
image = io.imread(url)


# In[42]:


def imshow(X, resize=None):
    resize(image, (100, 100)).shape
    pass


# In[ ]:




