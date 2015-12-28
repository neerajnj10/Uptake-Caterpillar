
# coding: utf-8


import sys
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import json

r = requests.get("http://api.glassdoor.com/api/api.htm?t.p=25738&t.k=iRCtcWJQamE&format=json&v=1&action=employers&q=uptake",
                 headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.content, "lxml")
soup.prettify

pElems = soup.select('p')
pw= pElems[0].getText()
data = json.loads(pw)
print(json.dumps(data))
print(data)

name= (data['response']['employers'][0]['name'])
name

website= (data['response']['employers'][0]['website'])
website

industry= (data['response']['employers'][0]['industry'])
industry

nor= (data['response']['employers'][0]['numberOfRatings'])
nor

ovr= (data['response']['employers'][0]['overallRating'])
ovr

ratdesc= (data['response']['employers'][0]['ratingDescription'])
ratdesc

culvalue= (data['response']['employers'][0]['cultureAndValuesRating'])
culvalue

senior= (data['response']['employers'][0]['seniorLeadershipRating'])
senior

comben= (data['response']['employers'][0]['compensationAndBenefitsRating'])
comben

career= (data['response']['employers'][0]['careerOpportunitiesRating'])
career

work= (data['response']['employers'][0]['workLifeBalanceRating'])
work

recom= (data['response']['employers'][0]['recommendToFriendRating'])
recom

industryName= (data['response']['employers'][0]['industryName'])
industryName

reviewdate= (data['response']['employers'][0]['featuredReview']['reviewDateTime'])
reviewdate

location= (data['response']['employers'][0]['featuredReview']['location'])
location

headline= (data['response']['employers'][0]['featuredReview']['headline'])
headline

pros= (data['response']['employers'][0]['featuredReview']['pros'])
pros

cons= (data['response']['employers'][0]['featuredReview']['cons'])
cons

overall= (data['response']['employers'][0]['featuredReview']['overall'])
overall

ceoname= (data['response']['employers'][0]['ceo']['name'])
ceoname

ceotitle = (data['response']['employers'][0]['ceo']['title'])
ceotitle

ceorating= (data['response']['employers'][0]['ceo']['numberOfRatings'])
ceorating


###create a dictionary to transport to mongodb.

dict = {'Name': name, 'Website': website, 'Industry': industry, 'No_Rating':nor, 'OVRating':ovr,'RatingDesc':ratdesc,
       'Culturevalue' : culvalue,
        'Senior' : senior,'Compensationandbenefits' : comben, 'Career' : career, 'Work' : work, 
        'Recommendation':recom, 'IndustryName':industryName,'Reviewdate':reviewdate,'Location':location, 
        'Headline':headline,'Pros':pros,'Cons':cons, 'OverallCeorating':overall,
       'CeoName':ceoname, 'CeoTitle':ceotitle,'CeoRating':ceorating};
dict


#install mongodb. make a directory 'data' inside mongodb folder, then initiatie mongoDB instance.
#C:\MongoDB>bin\mongod --dbpath data1 --port 27026

#now connect using python --- pymongo.

from pymongo import MongoClient

#we specify the localhost connection at port `27026` 

client = MongoClient("mongodb://localhost:27026/")

#database.
db = client['uptake']

#collections for  database.
collections = db['uptake_glassdoor']

#inserting data into database collection
collections.insert(dict)

#querying.
collections.find_one()

#database stats
db.command({'dbstats': 1})

#collections stats
db.command({'collstats': 'uptake_glassdoor'})

list(collections.find())

list(collections.find({'Name':'Uptake'}))

#inserting my data(reviews, rating etc/) into database.

collections.insert([  { 'CompanyForMe': 'Great Company', 'Myreviews_WorkPlace': 'looks good from reviews'}, {'Rating':5}
                ])

#data object has been successfully added. (see at the bottom.)
list(collections.find())

