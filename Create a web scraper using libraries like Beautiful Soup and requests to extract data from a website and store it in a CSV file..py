#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install beautifulsoup4 requests')


# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'id': 'example2'})
data = []
rows = table.find_all('tr')
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)
df = pd.DataFrame(data, columns=['#', 'Country (or dependency)', 'Population (2023)', 'Yearly Change', 
                                 'Net Change', 'Density (P/Km²)', 'Land Area (Km²)', 'Migrants (net)', 
                                 'Fert. Rate', 'Med. Age', 'Urban Pop %', 'World Share'])
df.to_csv('world_population.csv', index=False)

print("Data has been saved to world_population.csv")


# In[14]:


import pandas as pd
df = pd.read_csv('world_population.csv')
df.head()


# In[ ]:




