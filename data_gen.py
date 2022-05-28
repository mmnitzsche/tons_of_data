# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta, date


def get_countries():

    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    countries = []

    for items in soup.find('table', class_='wikitable').find_all('tr'):
        data = items.find_all(['td'])
        try:
            country = data[0].a.text
            region = data[1].a.text
            gdp = "".join(filter(str.isdigit,data[2].text))
            gdp = data[2].text
        except:
            pass

        try:
            countries.append({'country': country,'region': region, 'gdp': gdp})
        except:
            pass

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


clothes_list = [
'T-shirt',
'Topics',
'Twitter',
'Videos',
'bag',
'belt',
'blouse',
'boots',
'bow-tie',
'bra',
'bracelet',
'briefs',
'cap',
'coat',
'dress',
'earrings',
'glasses',
'handkerchief',
'hat ',
'heels',
'jacket',
'jeans',
'necklace',
'pajamas',
'panties',
'performance',
'preferences',
'purse',
'raincoat',
'ring',
'scarf',
'shawl',
'shirt',
'shoes',
'shorts',
'skirt',
'socks',
'stockings',
'suit',
'sun hat',
'sunglasses',
'sweater',
'swimsuit',
'tanktop',
'tie',
'tracksuit',
'vest',
'wallet',
'watch',
'wool hat']

countries = get_countries()
df_countries = cleaning_countries(df=countries)
brand_list = get_companies()
countries_values = list(df_countries['country'].tolist())

sales_df = []

for c in range(99999):
    country = random.choice(countries_values)
    companies = random.choice(brand_list)
    clothes = random.choice(clothes_list)
    profit = round(random.uniform(1000,99999), 2)

    sales_df.append({'country':country,'companies':companies,'clothes':clothes,'profit':profit})


sales_df = pd.DataFrame(sales_df)
sales_df
  
