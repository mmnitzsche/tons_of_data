# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from random import random
from datetime import datetime, timedelta, date
from playwright.sync_api import sync_playwright
import re

#%%


clothes = []
url = 'https://lingokids.com/english-for-kids/clothes'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for items in soup.find_all('span'):
    c = items.text
    clothes.append(c)

clothes = set(clothes)
clothes


clothes = ['T-shirt',
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
 'wool hat',]