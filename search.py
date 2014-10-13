from bs4 import BeautifulSoup
from urllib import urlopen #to read files
import google
import re

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


def search_who(question):
    g = google.search(question,num=5,stop=5)
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

    print max(people, key=people.get)


def search_where(question):
    g = google.search(question,num=2,stop=2)
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

    for p in pages:#list of lists
        for place in p:
            if place in countries.keys():
                #print place
                if place not in places.keys():
                    places[place] = 1
                else:
                    places[place]+= 1
    print places.keys()

    #for p in places.keys():
    #    print p
    #    print places.get(p,None)
    print max(places, key=places.get)


if __name__ == "__main__":
    search_who("who played batman")
    search_where("where is the effiel tower")
