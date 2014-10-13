from google import search
from urllib import urlopen
from bs4 import BeautifulSoup
import re

def verify_date(d):
    date = d.split()
    if date[1][-1] == ",":
        date[1] = date[1][:-1]
    r = re.compile("(Jan(uary)?|Feb(uary)?|Mar(ch)?|Apr(il)?|May|June?|July?|Aug(ust)?|Sep(t(ember)?)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)")
    try:
        return int(date[0]) <= 31 and r.match(date[1]) != None 
    except:
        return r.match(date[0]) != None and int(date[1]) <= 31


def search_date(query):

    #Date formats: MM/DD/YYYY | Aug 5, 2014 | 20 July 1980
    g = search(query,num=2,stop=2)

    results = []
    for url in g:
        u = urlopen(url)
        page = BeautifulSoup(u.read())
        results.append(page.get_text().replace("\n"," "))

    dates = { }
    date_res = []
    for page in results:
        #d = re.findall("(\d{1,2}\s[A-Z][a-z]+|[A-Z][a-z]+\s\d{1,2},)\s\d{4}",page)
        date_res.append(re.findall("\d{1,2}\s[A-Z][a-z]+\s\d{4}",page))
        date_res.append(re.findall("[A-Z][a-z]+\s\d{1,2},\s\d{4}",page))

    #print date_res
    for l in date_res:
        for date in l:
            if verify_date(date):
                if date not in dates.keys():
                    dates[date] = 1
                else:
                    dates[date] += 1

    print dates.keys()
    for date in dates.keys():
        if dates[date] > 2:
            print date + " " + str(dates[date])

    return max(dates, key=dates.get)

if __name__=="__main__":
    print search_date("When was the attack on pearl harbor?")
