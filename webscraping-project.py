from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font

webpage = 'https://coinmarketcap.com/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

tablecells = soup.findAll('tr')

for row in tablecells[1:6]:
    td = row.findAll('td')
    rank = td[1].text
    

    for name in tablecells:
        p = row.findAll('p')
        name = p[1].text

    # for image in tablecells:
    #     img = row.findAll('img')
    #     icon = img[0].

    for price in tablecells:
        span = row.findAll('span')
        price = float(span[0].text.replace('$','').replace(',',''))

    
    
    print(rank)
    print(name)
    print(price)
    # print(icon)
    # print(str(price))
    print()