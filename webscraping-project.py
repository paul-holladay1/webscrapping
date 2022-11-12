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
            price = float(span[3].text.replace('$','').replace(',',''))
            
        for per_change in tablecells:
            span = row.findAll('span')
            per_change = float(span[6].text.replace(',','').replace('%',''))
    
        # for carrot in tablecells():
        for carrot in row.findAll('span', class_ = "icon-Caret-up" and "icon-Caret-down"):
            # span = row.findAll('span', class_ = "icon-Caret-up" and "icon-Caret-down")
            if carrot == "icon-Caret-up":
                # diff = price * per_change
                # original_price = price - diff
                x = "up"
            if carrot == "icon-Caret-down":
                # diff = price * per_change
                # original_price = price - diff
                x = "down"

    
    print(f'Rank: {rank}')
    print(f'Name: {name}')
    print(f'Price: ${price:,.2f}')
    print(f'% Change in Last 24hrs: {per_change}%')
    print(f'Status: {x}')
    print()

