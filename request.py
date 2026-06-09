import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


base_url = 'https://api.jikan.moe/v4/anime'

params = {
    'unapproved': 'false',
    'q': 'jujutsu kaisen'
}

response = requests.get(url=base_url,params=params)

if response.status_code != 200:
    raise ValueError(response.status_code)

full_data = response.json()

clean_data = full_data['data']

df = pd.json_normalize(clean_data)


print(df.head(10))