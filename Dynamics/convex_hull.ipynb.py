#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
import numpy as np


# In[10]:


from scipy.spatial import ConvexHull

points = np.random.rand(30, 2)   # 30 random points in 2-D
hull = ConvexHull(points)
     


# In[13]:


figure()
plot(points[:,0], points[:,1], 'o')
hull_points = np.vstack([points[hull.vertices], points[hull.vertices[0]]])
plot(hull_points[:,0], hull_points[:,1], '-o')
show()    

