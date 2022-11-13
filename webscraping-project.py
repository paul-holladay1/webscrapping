from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

page = urlopen(url)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

tablecells = soup.findAll('tr')

for row in tablecells[1:6]:
    td = row.findAll('td')
    rank = td[1].text
    

    for name in tablecells:
        p = name.findAll('p')
        name = p[1].text

    # for image in tablecells:
    #     img = row.findAll('img')
    #     icon = img[0].

        for price in tablecells:
            span = price.findAll('span')
            price = float(span[3].text.replace('$','').replace(',',''))
        
        for per_change in tablecells:
            span = per_change.findAll('span')
            per_change = float(span[6].text.replace(',','').replace('%',''))
    
        # # for carrot in tablecells():
        # for caret in row.findAll('span', class_ = "icon-Caret-up" and "icon-Caret-down"):
        #     # span = row.findAll('span', class_ = "icon-Caret-up" and "icon-Caret-down")
        #     if caret == "icon-Caret-up":
        #         # diff = price * per_change
        #         # original_price = price - diff
        #         x = "up"
        #     if caret == "icon-Caret-down":
        #         # diff = price * per_change
        #         # original_price = price - diff
        #         x = "down"


        for caret in tablecells:
            span = caret.findAll('span', class_ = "icon-Caret-up" and "icon-Caret-down")
            # caret = span[0]
            if span[1].class_ == "icon-Caret-up":
                x = "up"
            if span[1].class_ == "icon-Caret-down":
                x = 'down'

        


    print(f'Rank: {rank}')
    print(f'Name: {name}')
    print(f'Price: ${price:,.2f}')
    print(f'% Change in Last 24hrs: {per_change}%')
    print(f'Status: {x}')
    print()

