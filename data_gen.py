# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta, date

def get_worldcities():
    cities_df = pd.read_excel('worldcities.xlsx').dropna()

    # cities_df = cities_df.sort_values(by='population',ascending=False ).head(50)['city'].tolist()
    return cities_df


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
    df_countries = df_countries.replace({'country': {'SouthKorea': 'South Korea', 'UnitedKingdom': 'United Kingdom', 'UnitedStates': 'United States'}})

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


cities_df = get_worldcities()
countries = get_countries()
df_countries = cleaning_countries(df=countries)
brand_list = get_companies()
countries_values = list(df_countries['country'].tolist())


sales_df = []

for c in range(999):
    country = random.choice(countries_values)
    companies = random.choice(brand_list)
    clothes = random.choice(clothes_list)
    profit = (round(random.uniform(100,9999), 2) * round(random.uniform(0,9), 2))
    max_index = len(cities_df[cities_df['country'] == country].sort_values(by='population', ascending=False).head(10)['city'].tolist())
    city = cities_df[cities_df['country'] == country].sort_values(by='population', ascending=False).head(10)['city'].tolist()[np.random.randint(0,max_index)]
    sales_df.append({'country':country,'city':city,'companies':companies,'clothes':clothes,'profit':profit})


sales_df = pd.DataFrame(sales_df)
sales_df = sales_df.merge(df_countries).drop(columns='gdp')
sales_df