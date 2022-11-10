
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title



tablecells = soup.findAll('tr')


for row in tablecells[1:6]:
    td = row.findAll('td')
    rank = td[0].text
    movie_name = td[1].text
    total_gross = int(td[7].text.replace('$','').replace(',',''))
    distributor = td[9].text
    theaters = int(td[6].text.replace(',',''))

    avg_gross_theater = total_gross/theaters


    print(f'Rank: {rank}')
    print(f'Movie Name: {movie_name}')
    print(f'Total Gross: ${total_gross:,.2f}')
    print(f'Distributor: {distributor}')
    print(f'Avg. Gross/Theater: ${avg_gross_theater:,.2f}')
    print()
    print()




##
##
##
##

