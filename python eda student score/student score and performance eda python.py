#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


df = pd.read_csv(r"C:\Users\sharm\OneDrive\Documents\student_score.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.columns


# In[8]:


df.isnull().sum()


# In[9]:


df.duplicated().sum()


# In[10]:


df['gender'].unique()


# In[11]:


print(df['race_ethnicity'].unique())
print(df['race_ethnicity'].nunique())


# In[12]:


print(df['parental_level_of_education'].unique())
print(df['parental_level_of_education'].nunique())


# In[13]:


print(df['lunch'].unique())
print(df['lunch'].nunique())


# In[14]:


print(df['test_preparation_course'].unique())
print(df['test_preparation_course'].nunique())


# In[15]:


df['parental_level_of_education'].value_counts()


# In[16]:


df[df['parental_level_of_education']== 'some high school'].head(10)


# In[17]:


df[df['parental_level_of_education']== 'high school'].head(10)


# In[19]:


df['parental_level_of_education'] = df['parental_level_of_education'].replace('some high school', 'high school')


# In[20]:


df['parental_level_of_education'].value_counts()


# In[21]:


df['total_number'] = df['math_score'] + df['reading_score'] + df['writing_score']
df['average'] = df['total_number']/3
df.head()


# In[22]:


##Q1. who dominate in this data set male or female?


# In[23]:


count_gender = df['gender'].value_counts()
print(count_gender.reset_index().rename(columns = {'index':'gender', 'gender':'count'}))
plt.pie(count_gender, labels = count_gender.index, autopct = '%.2f%%')
plt.title('Distribution of Gender')
plt.show()


# In[24]:


##Q2. In race_ethnicity which group is high contribution?


# In[25]:


count_race_ethnicity = df['race_ethnicity'].value_counts()
print(count_race_ethnicity.reset_index().rename(columns = {'index':'race_ethnicity', 'race_ethnicity':'Race_Ethnicity'}))
plt.bar(count_race_ethnicity.index, count_race_ethnicity)
plt.title('Distribution of race_ethnicity')
plt.xlabel('race_ethnicity')
plt.ylabel('count')
plt.show()


# In[26]:


##Q3. Check the Parents level of education?


# In[27]:


count_parental_level_of_education = df['parental_level_of_education'].value_counts()
print(count_parental_level_of_education.reset_index().rename(columns = {'index':'parental_level_of_education', 'parental_level_of_education':'Parental_Level_of_Education'}))
plt.bar(count_parental_level_of_education.index, count_parental_level_of_education)
plt.title('Distribution of parental_level_of_education')
plt.xlabel('parental_level_of_education')
plt.ylabel('count')
plt.xticks(rotation = 45)
plt.show()


# In[28]:


##Q4. How many student take standard lunch?


# In[29]:


count_lunch = df['lunch'].value_counts()
print(count_lunch.reset_index().rename(columns = {'index':'lunch', 'lunch':'Lunch'}))
plt.bar(count_lunch.index, count_lunch)
plt.title('Distribution of lunch')
plt.xlabel('lunch')
plt.ylabel('count')
plt.show()


# In[31]:


##Q5. How many student complete test preparation?


# In[32]:


count_test_preparation_course = df['test_preparation_course'].value_counts()
print(count_test_preparation_course.reset_index().rename(columns = {'index':'test_preparation_course', 'test_preparation_course':'Test_Preparation_Course'}))
plt.bar(count_test_preparation_course.index, count_test_preparation_course)
plt.title('Distribution of test_preparation_course')
plt.xlabel('test_preparation_course')
plt.ylabel('count')
plt.show()


# In[33]:


##Q6- Can Parental level of education effect on children score?


# In[34]:


fig, axes = plt.subplots(3, 1, figsize=(14, 18))

score_columns = ['math_score', 'reading_score', 'writing_score']
titles = ['Math numbers by Parental Level of Education', 'Reading numbers by Parental Level of Education', 'Writing numbers by Parental Level of Education']

for i, score in enumerate(score_columns):
    sns.boxplot(x='parental_level_of_education', y=score, data=df, ax=axes[i], palette='Set2')
    axes[i].set_title(titles[i])
    axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=45)
    axes[i].set_xlabel('Parental Level of Education')
    axes[i].set_ylabel(score.capitalize().replace('_', ' '))

plt.tight_layout()
plt.show()


# In[35]:


##Q.7 Can race/ethnicity effect on student score?


# In[36]:


fig, axes = plt.subplots(3, 1, figsize=(14, 18))

score_columns = ['math_score', 'reading_score', 'writing_score']
titles = ['Math Numbers by Race/Ethnicity', 'Reading Numbers by Race/Ethnicity', 'Writing Numbers by Race/Ethnicity']

for i, score in enumerate(score_columns):
    sns.boxplot(x='race_ethnicity', y=score, data=df, ax=axes[i], palette='Set3', order=sorted(df['race_ethnicity'].unique()))
    axes[i].set_title(titles[i])
    axes[i].set_xlabel('Race/Ethnicity')
    axes[i].set_ylabel(score.capitalize().replace('_', ' '))

plt.tight_layout()
plt.show()


# In[37]:


##Q8. How many student's take zero marks, check math, writing and reading test?


# In[38]:


reading_zero = df[df['reading_score'] == 0]['average'].count()
writing_zero = df[df['writing_score'] == 0]['average'].count()
math_zero = df[df['math_score'] == 0]['average'].count()

print(f'Number of students with less than 20 marks in Maths: {math_zero}')
print(f'Number of students with less than 20 marks in Writing: {writing_zero}')
print(f'Number of students with less than 20 marks in Reading: {reading_zero}')


# In[39]:


##Q9. How many student's take less then 20 marks, check math, writing and reading test


# In[40]:


reading_less_20 = df[df['reading_score'] <= 20]['average'].count()
writing_less_20 = df[df['writing_score'] <= 20]['average'].count()
math_less_20 = df[df['math_score'] <= 20]['average'].count()

print(f'Number of students with less than 20 marks in Maths: {math_less_20}')
print(f'Number of students with less than 20 marks in Writing: {writing_less_20}')
print(f'Number of students with less than 20 marks in Reading: {reading_less_20}')


# In[41]:


##Q10.Which group top on average base on parental_level_of_education


# In[42]:


df.groupby('parental_level_of_education')['average'].mean().sort_values(ascending=False)


# In[ ]:




