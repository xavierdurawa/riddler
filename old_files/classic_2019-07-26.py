import pandas as pd 
import requests

url = 'https://state.1keydata.com/bordering-states-list.php'
html = requests.get(url, verify=False).content

all_tables = pd.read_html(html)
state_ border = all_tables[1][[0, 1]].loc[2:51]

state_ border[1] = state_ border[1].split(',')