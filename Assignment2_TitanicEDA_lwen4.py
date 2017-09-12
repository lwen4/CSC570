
# coding: utf-8

# In[24]:

import pandas as pd
get_ipython().magic(u'pylab inline')


# In[10]:

df = pd.read_csv("train.csv")


# In[11]:

df


# In[12]:

###Assignment1EDA-Liao Wen


# In[ ]:

#Categorical Variables: Sex, Cabin, Embarked.
#Continuous Variables: PassengerId, Survived, Pclass, Age, SibSp, Parch, Fare.


# In[34]:

df.PassengerId.value_counts()


# In[46]:

df[df.PassengerId.isnull()]


# In[ ]:

#No missing value


# In[33]:

df.PassengerId.value_counts().plot(kind='hist')


# In[36]:

df.Survived.value_counts()


# In[47]:

df[df.Survived.isnull()]


# In[ ]:

#No missing value


# In[35]:

df.Survived.value_counts().plot(kind='hist')


# In[15]:

df.Pclass.value_counts()


# In[49]:

df[df.Pclass.isnull()]


# In[ ]:

#No missing value


# In[37]:

df.Pclass.value_counts().plot(kind='hist')


# In[16]:

df.Sex.value_counts()


# In[50]:

df[df.Sex.isnull()]


# In[ ]:

#No missing value


# In[38]:

df.Sex.value_counts().plot(kind='hist')


# In[17]:

df.Age.value_counts()


# In[51]:

df[df.Age.isnull()]


# In[ ]:

#177 Missing values found


# In[39]:

df.Age.value_counts().plot(kind='hist')


# In[18]:

df.SibSp.value_counts()


# In[52]:

df[df.SibSp.isnull()]


# In[ ]:

#No missing value


# In[40]:

df.SibSp.value_counts().plot(kind='hist')


# In[19]:

df.Parch.value_counts()


# In[53]:

df[df.Parch.isnull()]


# In[ ]:

#No missing value


# In[41]:

df.Parch.value_counts().plot(kind='hist')


# In[20]:

df.Ticket.value_counts()


# In[54]:

df[df.Ticket.isnull()]


# In[ ]:

#No missing value


# In[42]:

df.Ticket.value_counts().plot(kind='hist')


# In[21]:

df.Fare.value_counts()


# In[55]:

df[df.Fare.isnull()]


# In[ ]:

#No missing value


# In[43]:

df.Fare.value_counts().plot(kind='hist')


# In[22]:

df.Cabin.value_counts()


# In[56]:

df[df.Cabin.isnull()]


# In[ ]:

#687 missing values found


# In[44]:

df.Cabin.value_counts().plot(kind='hist')


# In[57]:

df.Embarked.value_counts()


# In[58]:

df[df.Embarked.isnull()]


# In[ ]:

#Two missing values found


# In[45]:

df. Embarked.value_counts().plot(kind='hist')


# In[ ]:

#Min, Max, Mean, and Standard Deviation of the continuous variables.


# In[61]:

df.describe()


# In[ ]:



