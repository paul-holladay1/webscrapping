from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font

url = 'https://crypto.com/price'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

tablecells = soup.findAll('tr')


for row in tablecells[1:6]:
    td = row.findAll('td')
    rank = td[1].text

    p = row.findAll('p')
    name = p[0].text

    div = row.findAll('div')
    price = float(div[8].text.replace('$','').replace(',',''))

    p = row.findAll('p')
    per_change = float(p[2].text.replace(',','').replace('%',''))

    if price > 0:
        diff = price * (per_change / 100)
        org_price = price - diff
    if price < 0:
        diff = price * (per_change / 100)
        org_price = price + diff




    print(f'Rank: {rank}')
    print(f'Name: {name}')
    print(f'Price: ${price:,.2f}')
    print(f'Percent Change per 24hrs: {per_change}%')
    print(f'Original Price: ${org_price:,.2f}')
    print()


    # Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for BTC 
    # and $3,000 for ETH.



    if name == 'Bitcoin' and price < 40000:
        message = "ALERT! " + name + " has fallen below $40,000." + "\n\n" + "Its current price is " + str(price) + "."
    if name == 'Ethereum' and price < 3000:
        message = "ALERT! " + name + " has fallen below $3,000." + "\n\n" + "Its current price is " + str(price) + "."


    import keys2
    from twilio.rest import Client

    client = Client(keys2.accountSID,keys2.authToken)

    TwilioNumber = '+12284600109'

    myCellPhone = '+12108678986'

    textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=message)


