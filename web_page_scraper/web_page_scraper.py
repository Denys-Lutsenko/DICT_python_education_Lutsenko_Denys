import requests
from bs4 import BeautifulSoup


url = input("Input the URL: ")
response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
content = BeautifulSoup(response.content, 'html.parser')
title = content.title.text
imdb = content.find('meta', {'property': "imdb:pageType"})
description = content.find('meta', {'name': 'description'})
if description is not None:
    description = content.find('meta', {'name': 'description'}).get('content')
total = {'title': title, 'description': description}
if description is None or imdb is None:
    print('Invalid movie page!')
else:
    print(total)