from google import search
from urllib import urlopen
from bs4 import BeautifulSoup
import re

def verify_date(d):
    date = d.split()
    r = re.compile("(Jan(uary)?|Feb(uary)?|Mar(ch)?|Apr(il)?|May|June?|July?|Aug(ust)?|Sep(t(ember)?)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)")
    return int(date[0]) <= 31 and r.match(date[1]) != None 

g = search("When was the first world cup",num=2,stop=2,pause=1.0)

#Date formats: MM/DD/YYYY | Aug 5, 2014 | 20 July 1980

results = []
for url in g:
    u = urlopen(url)
    page = BeautifulSoup(u.read())
    results.append(page.get_text().replace("\n"," "))

dates = { }
for page in results:
    #d = re.findall("(\d{1,2}\s[A-Z][a-z]+|[A-Z][a-z]+\s\d{1,2},)\s\d{4}",page)
    d = re.findall("\d{1,2}\s[A-Z][a-z]+\s\d{4}",page)

    for date in d:
        if(verify_date(date)):
            if date not in dates.keys():
                dates[date] = 1
            else:
                dates[date] += 1

#print dates
for date in dates.keys():
    if dates[date] > 2:
        print date + " " + str(dates[date])

