import tweepy
import time
import sys

from bs4 import *


import urllib2

CONSUMER_KEY = 'Insert Your Credentials here'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Insert Your Credentials here'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'Insert Your Credentials here'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'Insert Your Credentials here'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
names = []
page = "http://www.imdb.com/list/ls058011111/?start=1&view=compact&sort=listorian:asc&scb=0.6273764297118374"
page2 = "http://www.imdb.com/list/ls058011111/?start=251&view=compact&sort=listorian:asc"
page3 = "http://www.imdb.com/list/ls058011111/?start=501&view=compact&sort=listorian:asc"
page4 = "http://www.imdb.com/list/ls058011111/?start=751&view=compact&sort=listorian:asc"


def addNames(pages):
    url = urllib2.urlopen(pages)

    soup = BeautifulSoup(url)

    nameList = soup.findAll('td', 'name')
    for x in nameList:
        names.append(x.string.encode("utf-8"))

allActorArr = []
bodyParts =["face", "hair", "skin", "eyebrow", "eyelash", "ear", "nose", "mole", "lip", "chin", "forehead", "temple", "eye", "cheek", "nostril", "mouth", "jaw"]
import csv
with open('Sheet 1-Table 1-1.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for x in spamreader:
        print spamreader
        allActorArr.append(x[0])

print allActorArr
contra = ["but","with no", "with x for y","with two"]
butList = ["your 'parts' explode", "you can't tell anyone","you have to eat your ","you have to eat their "]
import random
def randomItemGenerator(arr):
    x = random.randint(0, arr.__len__()-1)
    print arr[x]
    return arr[x]
randomItemGenerator(allActorArr)
randomItemGenerator(bodyParts)
print "WWYD:" + randomItemGenerator(allActorArr) + " With no " + randomItemGenerator(bodyParts) + " OR " + randomItemGenerator(allActorArr) + " With no " + randomItemGenerator(bodyParts)
def generator():
    endStr = randomItemGenerator(allActorArr)
    endStr += (" " + contraParser(randomItemGenerator(contra)))
    return endStr

def contraParser(str):
    if(str == contra[0]):
        return contra[0] +" "+ butListParse(randomItemGenerator(butList))
    elif(str == contra[1]):
        return contra[1] +" "+ randomItemGenerator(bodyParts)
    elif(str == contra[2]):
        return ("with" +" "+ randomItemGenerator(bodyParts)+"'s" + " for" +" "+ randomItemGenerator(bodyParts)+"'s")
    else:
        return contra[3] +" "+ randomItemGenerator(bodyParts)+"'s"
def butListParse(str):
    if(str.__contains__("eat")):
        return str + randomItemGenerator(bodyParts)
    else:
        return str
print generator()
def fullGen():
    return "WWYD: " + generator() + " OR " + generator()

print fullGen()
def main():
    while(True):
        api.update_status(status=fullGen())
        time.sleep(900)
main()
