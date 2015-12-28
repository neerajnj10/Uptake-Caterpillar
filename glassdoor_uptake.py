
# coding: utf-8

# In[107]:

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



# In[108]:

pElems = soup.select('p')
pw= pElems[0].getText()
data = json.loads(pw)
print(json.dumps(data))
print(data)


# In[109]:

name= (data['response']['employers'][0]['name'])
name


# In[110]:

website= (data['response']['employers'][0]['website'])
website


# In[111]:

industry= (data['response']['employers'][0]['industry'])
industry


# In[112]:

nor= (data['response']['employers'][0]['numberOfRatings'])
nor


# In[113]:

ovr= (data['response']['employers'][0]['overallRating'])
ovr


# In[114]:

ratdesc= (data['response']['employers'][0]['ratingDescription'])
ratdesc


# In[115]:

culvalue= (data['response']['employers'][0]['cultureAndValuesRating'])
culvalue


# In[116]:

senior= (data['response']['employers'][0]['seniorLeadershipRating'])
senior


# In[117]:

comben= (data['response']['employers'][0]['compensationAndBenefitsRating'])
comben


# In[118]:

career= (data['response']['employers'][0]['careerOpportunitiesRating'])
career


# In[119]:

work= (data['response']['employers'][0]['workLifeBalanceRating'])
work


# In[120]:

recom= (data['response']['employers'][0]['recommendToFriendRating'])
recom


# In[121]:

industryName= (data['response']['employers'][0]['industryName'])
industryName


# In[122]:

reviewdate= (data['response']['employers'][0]['featuredReview']['reviewDateTime'])
reviewdate


# In[123]:

location= (data['response']['employers'][0]['featuredReview']['location'])
location


# In[124]:

headline= (data['response']['employers'][0]['featuredReview']['headline'])
headline


# In[125]:

pros= (data['response']['employers'][0]['featuredReview']['pros'])
pros


# In[126]:

cons= (data['response']['employers'][0]['featuredReview']['cons'])
cons


# In[127]:

overall= (data['response']['employers'][0]['featuredReview']['overall'])
overall


# In[128]:

ceoname= (data['response']['employers'][0]['ceo']['name'])
ceoname


# In[129]:

ceotitle = (data['response']['employers'][0]['ceo']['title'])
ceotitle


# In[149]:

ceorating= (data['response']['employers'][0]['ceo']['numberOfRatings'])
ceorating


# In[162]:

dict = {'Name': name, 'Website': website, 'Industry': industry, 'No_Rating':nor, 'OVRating':ovr,'RatingDesc':ratdesc,
       'Culturevalue' : culvalue,
        'Senior' : senior,'Compensationandbenefits' : comben, 'Career' : career, 'Work' : work, 
        'Recommendation':recom, 'IndustryName':industryName,'Reviewdate':reviewdate,'Location':location, 
        'Headline':headline,'Pros':pros,'Cons':cons, 'OverallCeorating':overall,
       'CeoName':ceoname, 'CeoTitle':ceotitle,'CeoRating':ceorating};
dict


# In[163]:

#install mongodb. make a directory 'data' inside mongodb folder, then initiatie mongoDB instance.
#C:\MongoDB>bin\mongod --dbpath data1 --port 27026

#now connect using python --- pymongo.


from pymongo import MongoClient

#we specify the localhost connection at port `27026` 

client = MongoClient("mongodb://localhost:27026/")

# spainsoccer is our databse we have created
db = client['uptake']

# liga_data is the collection we have created. Collections are documents inside the databases that stores the actual data. A single 
#database can have several collections.

collections = db['uptake_glassdoor']

#using insert method to finally insert the data into our colelction-liga_data of spainsoccer database
collections.insert(dict)


# In[164]:

collections.find_one()


# In[165]:

#database stats
db.command({'dbstats': 1})


# In[166]:

#collections stats
db.command({'collstats': 'uptake_glassdoor'})


# In[171]:

list(collections.find())


# In[177]:

list(collections.find({'Name':'Uptake'}))


# In[179]:

#inserting my data(reviews, rating etc/) into database.

collections.insert([  { 'CompanyForMe': 'Great Company', 'Myreviews_WorkPlace': 'looks good from reviews'}, {'Rating':5}
                ])


# In[185]:

#data object has been successfully added. (see at the bottom.)
list(collections.find())


# In[ ]:



