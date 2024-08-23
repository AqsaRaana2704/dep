#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the dataset
df = pd.read_csv('D:/countries of the world.csv')
df.head()


# In[17]:


df.tail()


# In[4]:


# Check the data types of the columns
df.dtypes


# In[7]:


# Convert columns to string if necessary
df['Population'] = df['Population'].astype(str)
df['Area (sq. mi.)'] = df['Area (sq. mi.)'].astype(str)
df['GDP ($ per capita)'] = df['GDP ($ per capita)'].astype(str)
df['Literacy (%)'] = df['Literacy (%)'].astype(str)

# Clean the columns: Remove commas and convert to numeric
df['Population'] = pd.to_numeric(df['Population'].str.replace(',', ''), errors='coerce')
df['Area (sq. mi.)'] = pd.to_numeric(df['Area (sq. mi.)'].str.replace(',', ''), errors='coerce')
df['GDP ($ per capita)'] = pd.to_numeric(df['GDP ($ per capita)'].str.replace(',', ''), errors='coerce')
df['Literacy (%)'] = pd.to_numeric(df['Literacy (%)'].str.replace(',', ''), errors='coerce')

# Check for any remaining NaN values
print("NaN values:", df.isnull().sum())

# Drop any rows with missing data in critical columns
df_cleaned = df.dropna(subset=['Population', 'Area (sq. mi.)', 'GDP ($ per capita)', 'Literacy (%)'])

# Verify data types after cleaning
print(df_cleaned.dtypes)


# In[9]:


import matplotlib.pyplot as plt
import seaborn as sns

# Population Distribution
plt.figure(figsize=(12, 6))
sns.histplot(df_cleaned['Population'], bins=50, kde=True)
plt.title('Population Distribution')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.show()

# GDP vs. Literacy Rate
plt.figure(figsize=(12, 6))
sns.scatterplot(x='GDP ($ per capita)', y='Literacy (%)', data=df_cleaned)
plt.title('GDP vs. Literacy Rate')
plt.xlabel('GDP ($ per capita)')
plt.ylabel('Literacy Rate (%)')
plt.show()



# In[13]:


# Top 10 Countries by Population
top_10_population = df_cleaned.nlargest(10, 'Population')
plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='Population', data=top_10_population)
plt.title('Top 10 Countries by Population')
plt.xticks(rotation=45)
plt.show()


# In[11]:


# Top 10 Countries by GDP per Capita
top_10_gdp = df_cleaned.nlargest(10, 'GDP ($ per capita)')
plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='GDP ($ per capita)', data=top_10_gdp)
plt.title('Top 10 Countries by GDP per Capita')
plt.xticks(rotation=45)
plt.show()

