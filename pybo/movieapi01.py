import os
from bs4 import BeautifulSoup
import requests


URL = "http://www.cgv.co.kr/movies/"
source = requests.get("http://www.cgv.co.kr/movies/").text
soup = BeautifulSoup(source, 'html.parser')

hotKeys = soup.select("div.sect-movie-chart")
hotKeys1 = soup.find_all('div','sect-movie-chart')

for key in hotKeys.find_all('strong'):
    print(div.get('title'))

for key in hotKeys1:
    print(key.select_one("strong.rank").get_text()
          + ". "
          + key.select_one("strong.title").get_text())

#print(hotKeys)