import requests
from bs4 import BeautifulSoup

res = requests.get('https://ja.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E6%BC%A2%E5%AD%97%E4%B8%80%E8%A6%A7')
soup = BeautifulSoup(res.text,"html.parser")
table = soup.find_all('tbody')
for row in table[1].find_all('tr')[1:]:
    if len(row.attrs) != 0:
        continue
    kanji = row.find_all('td')[1].text[0]
    print(kanji)