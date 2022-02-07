#!/usr/bin/env python
# coding: utf-8

# # 3. Linear Algebra
# 
# The two most important subjects for data science are _probability_ and _linear algebra_. This chapter deals with important concepts of linear algebra.
# 
# _This lesson talks about linear algebra from Data Science perspective_
# 
# #### Why do we need linear algebra in data science?
# 
# Consider a dataset of the crime rate of several cities as shown below, downloaded from [here](https://hastie.su.domains/StatLearnSparsity/data.html)

# In[1]:


import pandas as pd
df = pd.read_csv("https://hastie.su.domains/StatLearnSparsity_files/DATA/crime.txt", sep = '\t')
df.columns = ['X1','X2','X3','X4','X5','X6','X7']
df.head()


# * X1 = total overall reported crime rate per 1 million residents
# * X2 = reported violent crime rate per 100,000 residents
# * X3 = annual police funding in \$/resident
# * X4 = $\%$ of people 25 years+ with 4 yrs. of high school
# * X5 = $\%$ of 16 to 19 year-olds not in highschool and not highschool graduates.
# * X6 = $\%$ of 18 to 24 year-olds in college
# * X7 = $\%$ of people 25 years+ with at least 4 years of college

# 
