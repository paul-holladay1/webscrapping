import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#https://biblehub.com/asv/john/5.htm



random_chapter = random.randint(1,21)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

webpage = 'https://biblehub.com/asv/john/' + random_chapter + '.htm'

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

versus = soup.findAll('p', class_= 'reg')

print(versus)

# for verse in versus:
#     verse_list = verse.text.split('.')

# # print(verse_list)

# myverse = random.choice(verse_list[:-5])
 

# # print(f"Chapter: {random_chapter} , Verse: {myverse}")

# message = "Chapter:" + random_chapter + " Verse: " + myverse

# print(message)

# import keys2
# from twilio.rest import Client

# client = Client(keys2.accountSID,keys2.authToken)

# TwilioNumber = '+12284600109'

# myCellPhone = '+12108678986'

# textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,
#                 body=message)


# print(textmessage.status)