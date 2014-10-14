from google import search
from urllib import urlopen
from bs4 import BeautifulSoup
import re

stream = open("state.csv","r");
read = stream.read()
stream.close();
states = {}
states = dict.fromkeys(read.split("\n"),0);
#print states.keys()

stream1 = open("countries.csv","r");
read1 = stream1.read()
stream1.close();
countries = {}
countries = dict.fromkeys(read1.split("\n"),0);
#print countries.keys()

#stream to read our first names file
stream2 = open("firstnames.csv",'r')
read2 = stream2.read().replace("\n"," ")
stream2.close()

firstDic = {}
firstNames = read2.split() #all first names via our database
firstDic = dict.fromkeys(firstNames, 0)
   
#stream to read surnames file
stream3 = open("surnames.csv",'r')
read3 = stream3.read().replace("\n"," ")
stream3.close()

surnameList = []
surnameDic = {}
surnames = read3.split()
#setting up surname dictionary
for a in surnames:
    surnameDic[a.title()] = a.title()

#Verify that input is a valid date
def verify_date(d):
    date = d.split()
    if date[1][-1] == ",":
        date[1] = date[1][:-1]
    r = re.compile("(Jan(uary)?|Feb(uary)?|Mar(ch)?|Apr(il)?|May|June?|July?|Aug(ust)?|Sep(t(ember)?)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)")
    try:
        #Try to verify date (International format)
        return int(date[0]) <= 31 and r.match(date[1]) != None 
    except:
        #Verify date (American format)
        return r.match(date[0]) != None and int(date[1]) <= 31


def search_date(query):
    #Date formats: Aug 5, 2014 | 20 July 1980
    g = search(query,num=2,stop=2)

    #Grab text from result links
    results = []
    for url in g:
        u = urlopen(url)
        page = BeautifulSoup(u.read())
        results.append(page.get_text().replace("\n"," "))

    #Search text for dates and store them
    dates = { }
    date_res = []
    for page in results:
        #d = re.findall("(\d{1,2}\s[A-Z][a-z]+|[A-Z][a-z]+\s\d{1,2},)\s\d{4}",page)
        date_res.append(re.findall("\d{1,2}\s[A-Z][a-z]+\s\d{4}",page))
        date_res.append(re.findall("[A-Z][a-z]+\s\d{1,2},\s\d{4}",page))

    #Check if date is actually a date
    #Count frequency of dates 
    #print date_res
    for l in date_res:
        for date in l:
            if verify_date(date):
                if date not in dates.keys():
                    dates[date] = 1
                else:
                    dates[date] += 1

    ''' 
    print dates.keys()
    for date in dates.keys():
        if dates[date] > 2:
            print date + " " + str(dates[date])
    '''
    #return most frequent date found
    return max(dates, key=dates.get)
    

def search_who(question):
    g = search(question,num=5,stop=5)
    info = []
    htmls = [x for x in g]
    for url in htmls:
        u = urlopen(url)
        item = BeautifulSoup(u.read())
        item = item.get_text().replace("\n"," ")
        info.append(item)
    #print info

    people = {}
    pages = []
    for a in info:
        pages.append(re.findall("[A-Z][a-z]+\s[A-Z][a-z]+",a))
        #pages.append(re.findall("[A-Z][a-z]+\s([A-Z][a-z]+\s)?[A-Z][a-z]+",a))
    #print pages
    
    for p in pages:#list of lists
        for peep in p:
            #print peep
            firstLast= peep.split()#"Angela Lin" -> ["Angela","Lin"]
            if firstLast[0] in firstDic.keys() and firstLast[1] in surnameDic.keys():
                if peep not in people.keys():
                    people[peep] = 1
                else:
                    people[peep]+= 1
                    
    #print people.keys();
    #for p in people.keys():
    #    print p
    #    print people.get(p,None)

    return max(people, key=people.get)

def search_list(question):
    g = search(question,num=5,stop=5)
    # ret = ""
    # for x in g:
    #     ret =  ret + x  + "\n"
    # ret = "Here are links associated with '" + question + "':\n" + ret
    # print ret
    return g

def search_where(question):
    g = search(question,num=2,stop=2)
    info = []
    htmls = [x for x in g]
    for url in htmls:
        u = urlopen(url)
        item = BeautifulSoup(u.read())
        item = item.get_text().replace("\n"," ")
        info.append(item)
    #print info

    places = {}
    pages = []
    for a in info:
        pages.append(re.findall("[A-Z][a-z]+",a))
        pages.append(re.findall("Papua New Guinea",a))
        pages.append(re.findall("[A-Z][a-z]+\s[A-Z][a-z]+",a))
        pages.append(re.findall("State of Palestine",a))
        pages.append(re.findall("Democratic Republic of Congo",a)) 
        pages.append(re.findall("[A-Z][a-z]+\sRepublic",a)) 
        pages.append(re.findall("[A-Z][a-z]+\sIsland(s)?",a))
        pages.append(re.findall("Central African Republic",a))
    #print pages
    for p in pages:#list of lists
        for place in p:
            if place in countries.keys() or place in states.keys():
                #print place
                if place not in places.keys():
                    places[place] = 1
                else:
                    places[place]+= 1
    #print places.keys()

    #for p in places.keys():
    #    print p
    #    print places.get(p,None)
    return max(places, key=places.get)

#if __name__=="__main__":
    #print search_date("When was the attack on pearl harbor?")
    #print search_date("when was d day")
    #print search_list("who played batman")   
    #print search_where("where is the grand canyon")
