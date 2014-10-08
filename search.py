from bs4 import BeautifulSoup
from urllib import urlopen #to read files
import google
import re


g = google.search("Who played Chase on House",lang='en',num=2,start=0,stop=5,pause=2.0)
#help(google.search)

htmls = [x for x in g]

info = []

for url in htmls:
    #print url
    u = urlopen(url)
    item = u.read()
    info.append(item)


print info
