#!/usr/bin/env python
# coding: utf-8

# # Seaborn Visualization Library

# In[10]:


import pandas as pd
ds=pd.read_csv('emptest.csv')
print(ds)
print(ds.head())


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


sns.violinplot(x='Age',data=ds)


# In[5]:


sns.violinplot(x='Salary',data=ds)


# In[6]:


sns.swarmplot(x='Salary',data=ds)


# In[7]:


sns.countplot(x='Salary',data=ds)


# In[8]:


sns.stripplot(x='Salary',data=ds)


# In[9]:


sns.catplot(x='Salary',data=ds)


# # IRIS FLOWER DATASET

# In[18]:


dsiris=pd.read_csv('Iris.csv')
print(dsiris)
print(dsiris.head())
sns.set(style='whitegrid')
ax=sns.stripplot(x='class', y='sepal length', data=dsiris)
plt.title('Graph')
plt.show()


# In[19]:


ax=sns.swarmplot(x='class', y='sepal length', data=dsiris)
plt.title('Graph')
plt.show()


# In[26]:


dsiris['class'].value_counts()


# In[27]:


sns.countplot(dsiris['class'])


# In[28]:


sns.get_dataset_names()


# In[29]:


titanicds=sns.load_dataset('titanic')
print(titanicds)


# In[31]:


titanicds.columns


# In[33]:


titanicds['class']


# In[34]:


titanicds['class'].value_counts()


# In[35]:


sns.countplot(titanicds['class'])


# In[36]:


g=sns.catplot(x='class',y='survived',hue='sex', data=titanicds,kind='bar')
plt.show()


# In[37]:


g=sns.catplot(x='class',y='survived',hue='sex', data=titanicds,kind='violin')
plt.show()


# In[8]:


sns.load_dataset('tips')


# In[9]:


tips=sns.load_dataset('tips')
print(tips.head())
sns.violinplot(x='total_bill',data=tips)
plt.show()


# In[45]:


sns.histplot(x='total_bill',data=tips, bins=20)


# In[48]:


sns.displot(tips['tip'], bins=10)


# In[10]:


sns.distplot(tips['total_bill'])


# In[11]:


sns.distplot(tips['total_bill'],bins=100)


# In[12]:


#kde-Kernel Density Extimation
sns.distplot(tips['total_bill'],bins=50, kde=False)


# In[13]:


sns.kdeplot(tips['total_bill'])


# In[15]:


sns.violinplot(x='total_bill',data=tips)


# In[17]:


sns.jointplot(data=tips, x='total_bill',y='tip')


# In[18]:


sns.rugplot(data=tips, x='tip')


# In[19]:


sns.rugplot(data=tips, x='total_bill',y='tip')


# In[21]:


sns.boxplot(x='day',y='total_bill',hue='smoker',palette='coolwarm', data=tips)


# In[22]:


sns.pairplot(tips)


# In[24]:


sns.catplot(x='day',y='total_bill',kind='box', data=tips)


# In[25]:


mpgds=sns.load_dataset('mpg')
mpgds


# In[26]:


sns.scatterplot(data=mpgds, x='mpg', y='weight')


# In[28]:


sns.lineplot("mpg", 'weight', data=mpgds)


# In[30]:


sns.relplot("mpg", 'weight', data=mpgds)


# In[31]:


sns.regplot("mpg", 'weight', data=mpgds)


# In[32]:


sns.boxplot(x='weight', data=mpgds)


# In[33]:


sns.boxplot(x='displacement', data=mpgds)


# In[36]:


sns.jointplot(data=mpgds, x='weight',y='mpg', kind='kde')    


# In[38]:


c


# In[39]:


sns.swarmplot(data=mpgds, x='origin',y='mpg') 


# In[40]:


sns.catplot(data=mpgds, x='origin',y='mpg', kind='box') 


# In[42]:


taxids=sns.load_dataset('taxis')
taxids


# In[44]:


taxids['payment'].value_counts()


# In[45]:


sns.countplot(x='payment', data=taxids)


# In[47]:


sns.lmplot('distance', 'fare',data=taxids,hue='payment')


# In[48]:


sns.lmplot('distance', 'fare',data=taxids,hue='payment', col='color')


# In[49]:


sns.boxplot('distance', 'fare',data=taxids,hue='payment')


# In[50]:


sns.get_dataset_names()


# In[51]:


flights=sns.load_dataset('flights')
flights


# In[52]:


flights=flights.pivot('month','year','passengers')


# In[54]:


flights


# In[55]:


ax=sns.heatmap(flights)
ax


# In[ ]:




