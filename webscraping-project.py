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
    
    for rec in tablecells:
        p = rec.findAll('p')
        name = p[1].text
    
    print(rank)
    print(name)