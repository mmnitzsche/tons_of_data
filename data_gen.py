#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from random import random
from datetime import datetime, timedelta, date


date.today() - timedelta(days=2000)
sampl = int(np.random.uniform(low=0, high=2000, size=(1,))[0])
sampl


def get_countries():
    global country
    global region
    global gdp
    global data

    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    countries = []
    # table = soup.find('table', class_='wikitable').find_all('tr')
    for items in soup.find('table', class_='wikitable').find_all('tr'):
        data = items.find_all(['td'])
        print(data)
        try:
            country = data[0].a.text
            region = data[1].a.text
            gdp = "".join(filter(str.isdigit,data[2].text))
            gdp = data[2].text
            
        except: IndexError
        countries.append({'country': country,'region': region, 'gdp': gdp})
    return countries

def cleaning_countries(df):
    df_countries = pd.DataFrame(df)
    df_countries = df_countries.drop_duplicates().dropna(how='all')
    df_countries = df_countries[~df_countries['gdp'].isin(['','N/A'])].replace(r'\s+|\\n','', regex=True).replace(to_replace=",", value="", regex=True)
    df_countries['gdp'] = df_countries['gdp'].astype(int)
    df_countries  = df_countries.sort_values(by='gdp', ascending=False).head(15)
    return df_countries

def get_companies():
    companies = []
    url ='https://brandirectory.com/rankings/apparel/table'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for brands in soup.find_all('td', {'data-label': "Name"}):
        brands = brands.text
        companies.append(brands)

    choosed_companies = companies[:13]
    return choosed_companies

countries = get_countries()
df_countries = cleaning_countries(df=countries)
brand_list = get_companies()
countries_values = df_countries['country'].tolist()


# %%

c_list = []
for c in range(90):
    country = random.choice(countries_values)
    companies = random.choice(brand_list)
    c_list.append({'country':country,'companies':companies})
    # print(c_list)

# c_list

df = pd.DataFrame(c_list)
df.value_counts()
  

# %%

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for items in soup.find('table', class_='wikitable').find_all('tr','a'):
    data = items.find_all(['td'])
    print(data[0].text)
print(data[0].text)
