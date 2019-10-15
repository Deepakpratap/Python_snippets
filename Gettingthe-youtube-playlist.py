'''
The below snippet is used for extracting data from the youtube channel
I have used BeautifulSoup and Request module to get the details for a youtube channel
In my case I have used Corey Schafer's youtube channel.
'https://www.youtube.com/user/schafer5'
Same can be used to extract data from other youtube user like sentdex
'https://www.youtube.com/user/sentdex'
This is a working prototype

'''
from bs4 import BeautifulSoup
import requests
import re
from collections import namedtuple
resp = requests.get('https://www.youtube.com/user/schafer5').text

soup = BeautifulSoup(resp, 'lxml')

playlist_url_list = namedtuple('playlist_details', ['playlist_id', 'play_title'])
container = []

for link in soup.find_all("a", href=re.compile("/playlist\?list")):
    url = link.get('href')
    i = playlist_url_list(url.split('/playlist?list=')[1], link.get('title'))
    container.append(i)

for i in container:
    id, title = i
    resp1 = requests.get(f'https://www.youtube.com/playlist?list={id}').text
    soup1 = BeautifulSoup(resp1, 'lxml')
    print('***************************************************')
    print('\n')
    print(f'The playlist *** {title} *** has below contents')
    print('---------------------------------------------------')

    for link in soup1.find_all('tr', class_="pl-video yt-uix-tile"):
        print(link.get('data-title'), 'Link : ', 'https://www.youtube.com/watch?v=' + link.get('data-video-id'))








