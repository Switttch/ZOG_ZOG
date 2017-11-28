
# coding: utf-8

# ZOG_ZOG2


get_ipython().system(' pip install Seaborn')


# In[2]:


import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb


# In[3]:


get_ipython().magic('matplotlib inline')
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')
