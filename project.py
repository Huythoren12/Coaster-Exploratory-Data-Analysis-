#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

plt.style.use('ggplot')

# Load data
df = pd.read_csv('C:\\Users\\HP\\Downloads\\coaster_db.csv')

# Select relevant columns
df = df[['coaster_name', 'Location', 'Status', 'Opening date',
         'Manufacturer', 'Opened', 'year_introduced', 'latitude',
         'longitude', 'Type_Main', 'opening_date_clean', 'speed_mph',
         'height_ft', 'Inversions_clean', 'Gforce_clean']].copy()


df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'], errors='coerce')


df.rename(columns={
    'coaster_name': 'Coaster_Name',
    'year_introduced': 'Year_Introduced',
    'opening_date_clean': 'Opening_Date_Clean',
    'speed_mph': 'Speed_Mph',
    'height_ft': 'Height_Ft',
    'Inversions_clean': 'Inversions',
    'Gforce_clean': 'Gforce'
}, inplace=True)


df = df.loc[~df.duplicated(subset=['Coaster_Name', 'Location', 'Opening_Date_Clean'])]\
       .reset_index(drop=True)

ax = df['Year_Introduced'].value_counts()\
       .head(10)\
       .plot(kind='bar',title='Top 10 Years Coasters Introduced') 
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')


# In[11]:


ax = df['Speed_Mph'].plot(kind='hist',  
                          bins=20,
                          title='Coaster Speed (mph)')
ax.set_xlabel('Speed (mph)')


# In[14]:


df.plot(kind='scatter',
        x='Speed_Mph',  
        y='Height_Ft',
        title='Coaster Speed vs Height')
plt.show()


# In[17]:


sns.scatterplot(x='Speed_Mph',
               y='Height_Ft',
                hue = 'Year_Introduced',
               data = df)


# In[19]:


sns.pairplot(df, vars=['Year_Introduced','Speed_Mph','Height_Ft','Inversions','Gforce'],
                hue = 'Type_Main')
plt.show()


# In[ ]:




