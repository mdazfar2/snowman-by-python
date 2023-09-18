#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[7]:


canvas=np.full((600,600,3),255,dtype=np.uint8)


# In[8]:


def display(photo):
    cv2.imshow("some",photo)
    cv2.waitKey()
    cv2.destroyAllWindows()


# In[9]:


for angle in np.arange(0, 2 * np.pi, 1/2/r):
  for i in range(109,112): 
    x = int( 435 + i * np.cos(angle))
    y = int( 300 + i * np.sin(angle))
    canvas[x,y] = [0]


# In[10]:


for angle in np.arange(0, 2 * np.pi, 1/2/r):
  for i in range(55,58): 
    x = int( 269 + i * np.cos(angle))
    y = int( 300 + i * np.sin(angle))
    canvas[x,y] = [0]


# In[11]:


for angle in np.arange(0, 2 * np.pi ,1/2/r):
  for i in range(0,5): 
    x = int( 249 + i * np.cos(angle))
    y = int( 275 + i * np.sin(angle))
    canvas[x,y] = [0]
    
    
for angle in np.arange(0, 2 * np.pi ,1/2/r):
  for i in range(0,5): 
    x = int( 249 + i * np.cos(angle))
    y = int( 325 + i * np.sin(angle))
    canvas[x,y] = [0]
    
for angle in np.arange(0, 2 * np.pi, 1/2/r):
  for i in range(0,5): 
    x = int( 435 + i * np.cos(angle))
    y = int( 300 + i * np.sin(angle))
    canvas[x,y] = [0]
    
for angle in np.arange(0, 2 * np.pi, 1/2/r):
  for i in range(0,5): 
    x = int( 400 + i * np.cos(angle))
    y = int( 300 + i * np.sin(angle))
    canvas[x,y] = [0]
    
for angle in np.arange(0, 2 * np.pi, 1/2/r):
  for i in range(0,5): 
    x = int( 470 + i * np.cos(angle))
    y = int( 300 + i * np.sin(angle))
    canvas[x,y] = [0]
    
for angle in np.arange((7 * np.pi/4)/2 + np.pi, (9 * np.pi/4)/2 + np.pi , 1/2/r): 
    x = int( 244 + 64 * np.cos(angle))
    y = int( 300 + 64 * np.sin(angle))
    canvas[x,y] = [0]


# In[12]:


for i in range(-5,5):
    canvas[224-i,300-65:300+65]=[0,0,255]


# In[13]:


canvas[149:220,300-50:300+50]=[0,0,225]
canvas[204:220,300-50:300+50]=[0]


# In[14]:


slope=np.tan(np.pi/4)
coeff= 390 - np.tan(np.pi/4)*230 
for i in  range(121,230):
    for j in range(0,4):
        canvas[int(slope*i + coeff+j)-13,i ] = [0]


# In[15]:


slope=np.tan(-np.pi/6)
coeff= 390 - np.tan(np.pi/6)*360 
for i in  range(360,451):
    for j in range(0,4):
        canvas[400+int(slope*i + coeff+j),i ] = [0]


# In[16]:


display(canvas)


# In[ ]:




