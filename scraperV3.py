from bs4 import BeautifulSoup
import requests

getter=requests.get('https://h1bdata.info/index.php?em=&job=backend+engineer&city=&year=2022').text
soup=BeautifulSoup(getter,'lxml')
jobs=soup.find_all('table',class_='tablesorter tablesorter-blue hasStickyHeaders')

   
with open('scrap.txt', 'w') as f:
    for head in jobs:
        f.write(head.get_text('td').replace('td','\n'))

headers = []
title_name=soup.find_all('th')
for i in title_name:
    title=i.text
    outp=headers.append(title)
    print(headers)


        