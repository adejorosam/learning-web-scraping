import requests
from bs4 import BeautifulSoup
import pandas as pd

start_url = 'https://en.wikipedia.org/wiki/Tesla%2C_Inc.'
downloaded_html = requests.get(start_url)
soup = BeautifulSoup(downloaded_html.text, 'html.parser')
# if soup != '':
#     print('Hi')
# else:
#     print('Holla!')

with open('downloaded.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
