#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)


# In[5]:


iris=pd.read_csv("Iris.csv")
iris.head()


# In[6]:


iris[0:9]


# In[7]:


iris[0:9:2]


# In[8]:


#Counting number of species
iris["species"].value_counts()


# In[11]:


iris.plot(kind="scatter", x="sepal_length", y="sepal_width")


# In[14]:


sns.FacetGrid(iris,hue="species",size=5)    .map(plt.scatter,"sepal_length","sepal_width")    .add_legend()


# In[17]:


sns.boxplot(x="species",y="petal_length",data=iris)


# In[25]:


ax=sns.boxplot(x="species",y="petal_length",data=iris)
ax=sns.stripplot(x="species",y="petal_length",jitter=True, data=iris,edgecolor="red")


# In[26]:


sns.violinplot(x="species",y="petal_length",data=iris,size=6)


# In[27]:


sns.FacetGrid(iris,hue="species",size=5).map(sns.kdeplot,"petal_length").add_legend()


# In[ ]:




