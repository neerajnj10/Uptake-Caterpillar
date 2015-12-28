

```python
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


```




    <bound method Tag.prettify of <html><body><p>{
      "success": true,
      "status": "OK",
      "jsessionid": "5AC394A4A46D0D2EC14ED3683FD6B630",
      "response": {
        "attributionURL": "http://www.glassdoor.com/Reviews/uptake-reviews-SRCH_KE0,6.htm",
        "currentPageNumber": 1,
        "totalNumberOfPages": 1,
        "totalRecordCount": 3,
        "employers": [
          {
            "id": 978686,
            "name": "Uptake",
            "website": "www.uptake.com",
            "isEEP": false,
            "exactMatch": true,
            "industry": "Computer Hardware &amp; Software",
            "numberOfRatings": 11,
            "squareLogo": "https://media.glassdoor.com/sqll/978686/uptake-squarelogo-1428439285033.png",
            "overallRating": 4.4,
            "ratingDescription": "Very Satisfied",
            "cultureAndValuesRating": "4.0",
            "seniorLeadershipRating": "3.9",
            "compensationAndBenefitsRating": "4.3",
            "careerOpportunitiesRating": "4.2",
            "workLifeBalanceRating": "4.2",
            "recommendToFriendRating": "0.8",
            "sectorId": 10013,
            "sectorName": "Information Technology",
            "industryId": 200060,
            "industryName": "Computer Hardware &amp; Software",
            "featuredReview": {
              "id": 8871105,
              "currentJob": true,
              "reviewDateTime": "2015-12-09 13:10:32.21",
              "jobTitle": "Employee",
              "location": "Chicago, IL",
              "headline": "Really exciting opportunity.",
              "pros": "Uptake is full of the most talented people with whom Iâve had the opportunity of working. Everyone genuinely cares about the rapid and successful growth of the company. \r\n\r\nWe have great benefits: unlimited paid time off, health/dental/vision/life, commuter benefits, gym discounts, the ability to work from home, lunch stipend Monday-Thursday and more.",
              "cons": "Weâre growing rapidly, so next steps can be unclear sometimes. We have many intelligent members of leadership who are trying to collaboratively establish our messaging, and disagreement presents challenges as we grow. I think this will work itself out over timeâweâre barely over a year old.",
              "overall": 5,
              "overallNumeric": 5
            },
            "ceo": {
              "name": "Brad Keywell",
              "title": "CEO",
              "numberOfRatings": 5,
              "pctApprove": 100,
              "pctDisapprove": 0
            }
          },
          {
            "id": 349690,
            "name": "UpTake Networks",
            "website": "www.uptake.com",
            "isEEP": false,
            "exactMatch": false,
            "industry": "Motion Picture Production &amp; Distribution",
            "numberOfRatings": 2,
            "squareLogo": "",
            "overallRating": 3.3,
            "ratingDescription": "OK",
            "cultureAndValuesRating": "3.0",
            "seniorLeadershipRating": "3.3",
            "compensationAndBenefitsRating": "2.1",
            "careerOpportunitiesRating": "2.8",
            "workLifeBalanceRating": "4.2",
            "recommendToFriendRating": "0.4",
            "sectorId": 10016,
            "sectorName": "Media",
            "industryId": 200077,
            "industryName": "Motion Picture Production &amp; Distribution",
            "featuredReview": {
              "id": 668162,
              "currentJob": false,
              "reviewDateTime": "2010-09-30 17:06:50.377",
              "jobTitle": "Employee",
              "location": "Palo Alto, CA",
              "headline": "UpTake Networks: up and comer in the competitive online travel industry",
              "pros": "Great strategy, nice traffic growth, good management team from Yahoo!, low *sshole quotient.  CEO and other execs are well connected in the travel industry",
              "cons": "Company is very focused on it's operational plan and path to profitability.  That means that there is less random experimentation than I would want.  However, this management discipline will enable the company to reach profitability.",
              "overall": 5,
              "overallNumeric": 5
            },
            "ceo": {
              "name": "Eric Lefkofsky and Ted Leonsis",
              "title": "CEO",
              "numberOfRatings": 0,
              "pctApprove": 0,
              "pctDisapprove": 0
            }
          },
          {
            "id": 286427,
            "name": "Uptake Medical",
            "website": "www.uptakemedical.com",
            "isEEP": false,
            "exactMatch": false,
            "industry": "Health Care Products Manufacturing",
            "numberOfRatings": 0,
            "squareLogo": "",
            "overallRating": 0,
            "ratingDescription": "Not Applicable",
            "cultureAndValuesRating": "0.0",
            "seniorLeadershipRating": "0.0",
            "compensationAndBenefitsRating": "0.0",
            "careerOpportunitiesRating": "0.0",
            "workLifeBalanceRating": "0.0",
            "recommendToFriendRating": "0.0",
            "sectorId": 10015,
            "sectorName": "Manufacturing",
            "industryId": 200072,
            "industryName": "Health Care Products Manufacturing"
          }
        ]
      }
    }</p></body></html>>




```python
pElems = soup.select('p')
pw= pElems[0].getText()
data = json.loads(pw)
print(json.dumps(data))
print(data)
```

    {"status": "OK", "response": {"totalRecordCount": 3, "attributionURL": "http://www.glassdoor.com/Reviews/uptake-reviews-SRCH_KE0,6.htm", "employers": [{"featuredReview": {"location": "Chicago, IL", "pros": "Uptake is full of the most talented people with whom I\u2019ve had the opportunity of working. Everyone genuinely cares about the rapid and successful growth of the company. \r\n\r\nWe have great benefits: unlimited paid time off, health/dental/vision/life, commuter benefits, gym discounts, the ability to work from home, lunch stipend Monday-Thursday and more.", "reviewDateTime": "2015-12-09 13:10:32.21", "overallNumeric": 5, "currentJob": true, "headline": "Really exciting opportunity.", "jobTitle": "Employee", "cons": "We\u2019re growing rapidly, so next steps can be unclear sometimes. We have many intelligent members of leadership who are trying to collaboratively establish our messaging, and disagreement presents challenges as we grow. I think this will work itself out over time\u2014we\u2019re barely over a year old.", "overall": 5, "id": 8871105}, "name": "Uptake", "sectorName": "Information Technology", "industry": "Computer Hardware & Software", "workLifeBalanceRating": "4.2", "careerOpportunitiesRating": "4.2", "ceo": {"title": "CEO", "name": "Brad Keywell", "pctApprove": 100, "numberOfRatings": 5, "pctDisapprove": 0}, "industryName": "Computer Hardware & Software", "compensationAndBenefitsRating": "4.3", "cultureAndValuesRating": "4.0", "website": "www.uptake.com", "overallRating": 4.4, "sectorId": 10013, "isEEP": false, "id": 978686, "squareLogo": "https://media.glassdoor.com/sqll/978686/uptake-squarelogo-1428439285033.png", "ratingDescription": "Very Satisfied", "industryId": 200060, "numberOfRatings": 11, "exactMatch": true, "recommendToFriendRating": "0.8", "seniorLeadershipRating": "3.9"}, {"featuredReview": {"location": "Palo Alto, CA", "pros": "Great strategy, nice traffic growth, good management team from Yahoo!, low *sshole quotient.  CEO and other execs are well connected in the travel industry", "reviewDateTime": "2010-09-30 17:06:50.377", "overallNumeric": 5, "currentJob": false, "headline": "UpTake Networks: up and comer in the competitive online travel industry", "jobTitle": "Employee", "cons": "Company is very focused on it's operational plan and path to profitability.  That means that there is less random experimentation than I would want.  However, this management discipline will enable the company to reach profitability.", "overall": 5, "id": 668162}, "name": "UpTake Networks", "sectorName": "Media", "industry": "Motion Picture Production & Distribution", "workLifeBalanceRating": "4.2", "careerOpportunitiesRating": "2.8", "ceo": {"title": "CEO", "name": "Eric Lefkofsky and Ted Leonsis", "pctApprove": 0, "numberOfRatings": 0, "pctDisapprove": 0}, "industryName": "Motion Picture Production & Distribution", "compensationAndBenefitsRating": "2.1", "cultureAndValuesRating": "3.0", "website": "www.uptake.com", "overallRating": 3.3, "sectorId": 10016, "isEEP": false, "id": 349690, "squareLogo": "", "ratingDescription": "OK", "industryId": 200077, "numberOfRatings": 2, "exactMatch": false, "recommendToFriendRating": "0.4", "seniorLeadershipRating": "3.3"}, {"name": "Uptake Medical", "squareLogo": "", "ratingDescription": "Not Applicable", "industry": "Health Care Products Manufacturing", "numberOfRatings": 0, "industryName": "Health Care Products Manufacturing", "workLifeBalanceRating": "0.0", "careerOpportunitiesRating": "0.0", "sectorName": "Manufacturing", "industryId": 200072, "recommendToFriendRating": "0.0", "compensationAndBenefitsRating": "0.0", "cultureAndValuesRating": "0.0", "website": "www.uptakemedical.com", "exactMatch": false, "isEEP": false, "sectorId": 10015, "seniorLeadershipRating": "0.0", "overallRating": 0, "id": 286427}], "currentPageNumber": 1, "totalNumberOfPages": 1}, "success": true, "jsessionid": "5AC394A4A46D0D2EC14ED3683FD6B630"}
    {'status': 'OK', 'response': {'totalRecordCount': 3, 'attributionURL': 'http://www.glassdoor.com/Reviews/uptake-reviews-SRCH_KE0,6.htm', 'employers': [{'featuredReview': {'location': 'Chicago, IL', 'pros': 'Uptake is full of the most talented people with whom Iâve had the opportunity of working. Everyone genuinely cares about the rapid and successful growth of the company. \r\n\r\nWe have great benefits: unlimited paid time off, health/dental/vision/life, commuter benefits, gym discounts, the ability to work from home, lunch stipend Monday-Thursday and more.', 'reviewDateTime': '2015-12-09 13:10:32.21', 'overallNumeric': 5, 'currentJob': True, 'headline': 'Really exciting opportunity.', 'jobTitle': 'Employee', 'cons': 'Weâre growing rapidly, so next steps can be unclear sometimes. We have many intelligent members of leadership who are trying to collaboratively establish our messaging, and disagreement presents challenges as we grow. I think this will work itself out over timeâweâre barely over a year old.', 'overall': 5, 'id': 8871105}, 'name': 'Uptake', 'sectorName': 'Information Technology', 'industry': 'Computer Hardware & Software', 'workLifeBalanceRating': '4.2', 'careerOpportunitiesRating': '4.2', 'ceo': {'title': 'CEO', 'name': 'Brad Keywell', 'pctApprove': 100, 'numberOfRatings': 5, 'pctDisapprove': 0}, 'industryName': 'Computer Hardware & Software', 'compensationAndBenefitsRating': '4.3', 'cultureAndValuesRating': '4.0', 'website': 'www.uptake.com', 'overallRating': 4.4, 'sectorId': 10013, 'isEEP': False, 'id': 978686, 'squareLogo': 'https://media.glassdoor.com/sqll/978686/uptake-squarelogo-1428439285033.png', 'ratingDescription': 'Very Satisfied', 'industryId': 200060, 'numberOfRatings': 11, 'exactMatch': True, 'recommendToFriendRating': '0.8', 'seniorLeadershipRating': '3.9'}, {'featuredReview': {'location': 'Palo Alto, CA', 'pros': 'Great strategy, nice traffic growth, good management team from Yahoo!, low *sshole quotient.  CEO and other execs are well connected in the travel industry', 'reviewDateTime': '2010-09-30 17:06:50.377', 'overallNumeric': 5, 'currentJob': False, 'headline': 'UpTake Networks: up and comer in the competitive online travel industry', 'jobTitle': 'Employee', 'cons': "Company is very focused on it's operational plan and path to profitability.  That means that there is less random experimentation than I would want.  However, this management discipline will enable the company to reach profitability.", 'overall': 5, 'id': 668162}, 'name': 'UpTake Networks', 'sectorName': 'Media', 'industry': 'Motion Picture Production & Distribution', 'workLifeBalanceRating': '4.2', 'careerOpportunitiesRating': '2.8', 'ceo': {'title': 'CEO', 'name': 'Eric Lefkofsky and Ted Leonsis', 'pctApprove': 0, 'numberOfRatings': 0, 'pctDisapprove': 0}, 'industryName': 'Motion Picture Production & Distribution', 'compensationAndBenefitsRating': '2.1', 'cultureAndValuesRating': '3.0', 'website': 'www.uptake.com', 'overallRating': 3.3, 'sectorId': 10016, 'isEEP': False, 'id': 349690, 'squareLogo': '', 'ratingDescription': 'OK', 'industryId': 200077, 'numberOfRatings': 2, 'exactMatch': False, 'recommendToFriendRating': '0.4', 'seniorLeadershipRating': '3.3'}, {'name': 'Uptake Medical', 'squareLogo': '', 'ratingDescription': 'Not Applicable', 'industry': 'Health Care Products Manufacturing', 'numberOfRatings': 0, 'industryName': 'Health Care Products Manufacturing', 'workLifeBalanceRating': '0.0', 'careerOpportunitiesRating': '0.0', 'sectorName': 'Manufacturing', 'industryId': 200072, 'recommendToFriendRating': '0.0', 'compensationAndBenefitsRating': '0.0', 'cultureAndValuesRating': '0.0', 'website': 'www.uptakemedical.com', 'exactMatch': False, 'isEEP': False, 'sectorId': 10015, 'seniorLeadershipRating': '0.0', 'overallRating': 0, 'id': 286427}], 'currentPageNumber': 1, 'totalNumberOfPages': 1}, 'success': True, 'jsessionid': '5AC394A4A46D0D2EC14ED3683FD6B630'}
    


```python
name= (data['response']['employers'][0]['name'])
name
```




    'Uptake'




```python
website= (data['response']['employers'][0]['website'])
website

```




    'www.uptake.com'




```python
industry= (data['response']['employers'][0]['industry'])
industry
```




    'Computer Hardware & Software'




```python
nor= (data['response']['employers'][0]['numberOfRatings'])
nor
```




    11




```python
ovr= (data['response']['employers'][0]['overallRating'])
ovr
```




    4.4




```python
ratdesc= (data['response']['employers'][0]['ratingDescription'])
ratdesc
```




    'Very Satisfied'




```python
culvalue= (data['response']['employers'][0]['cultureAndValuesRating'])
culvalue
```




    '4.0'




```python
senior= (data['response']['employers'][0]['seniorLeadershipRating'])
senior
```




    '3.9'




```python
comben= (data['response']['employers'][0]['compensationAndBenefitsRating'])
comben
```




    '4.3'




```python
career= (data['response']['employers'][0]['careerOpportunitiesRating'])
career
```




    '4.2'




```python
work= (data['response']['employers'][0]['workLifeBalanceRating'])
work
```




    '4.2'




```python
recom= (data['response']['employers'][0]['recommendToFriendRating'])
recom
```




    '0.8'




```python
industryName= (data['response']['employers'][0]['industryName'])
industryName
```




    'Computer Hardware & Software'




```python
reviewdate= (data['response']['employers'][0]['featuredReview']['reviewDateTime'])
reviewdate
```




    '2015-12-09 13:10:32.21'




```python
location= (data['response']['employers'][0]['featuredReview']['location'])
location
```




    'Chicago, IL'




```python
headline= (data['response']['employers'][0]['featuredReview']['headline'])
headline
```




    'Really exciting opportunity.'




```python
pros= (data['response']['employers'][0]['featuredReview']['pros'])
pros
```




    'Uptake is full of the most talented people with whom Iâve had the opportunity of working. Everyone genuinely cares about the rapid and successful growth of the company. \r\n\r\nWe have great benefits: unlimited paid time off, health/dental/vision/life, commuter benefits, gym discounts, the ability to work from home, lunch stipend Monday-Thursday and more.'




```python
cons= (data['response']['employers'][0]['featuredReview']['cons'])
cons
```




    'Weâre growing rapidly, so next steps can be unclear sometimes. We have many intelligent members of leadership who are trying to collaboratively establish our messaging, and disagreement presents challenges as we grow. I think this will work itself out over timeâweâre barely over a year old.'




```python
overall= (data['response']['employers'][0]['featuredReview']['overall'])
overall
```




    5




```python
ceoname= (data['response']['employers'][0]['ceo']['name'])
ceoname
```




    'Brad Keywell'




```python
ceotitle = (data['response']['employers'][0]['ceo']['title'])
ceotitle
```




    'CEO'




```python
ceorating= (data['response']['employers'][0]['ceo']['numberOfRatings'])
ceorating
```




    5




```python
dict = {'Name': name, 'Website': website, 'Industry': industry, 'No_Rating':nor, 'OVRating':ovr,'RatingDesc':ratdesc,
       'Culturevalue' : culvalue,
        'Senior' : senior,'Compensationandbenefits' : comben, 'Career' : career, 'Work' : work, 
        'Recommendation':recom, 'IndustryName':industryName,'Reviewdate':reviewdate,'Location':location, 
        'Headline':headline,'Pros':pros,'Cons':cons, 'OverallCeorating':overall,
       'CeoName':ceoname, 'CeoTitle':ceotitle,'CeoRating':ceorating};
dict

```




    {'Career': '4.2',
     'CeoName': 'Brad Keywell',
     'CeoRating': 5,
     'CeoTitle': 'CEO',
     'Compensationandbenefits': '4.3',
     'Cons': 'Weâre growing rapidly, so next steps can be unclear sometimes. We have many intelligent members of leadership who are trying to collaboratively establish our messaging, and disagreement presents challenges as we grow. I think this will work itself out over timeâweâre barely over a year old.',
     'Culturevalue': '4.0',
     'Headline': 'Really exciting opportunity.',
     'Industry': 'Computer Hardware & Software',
     'IndustryName': 'Computer Hardware & Software',
     'Location': 'Chicago, IL',
     'Name': 'Uptake',
     'No_Rating': 11,
     'OVRating': 4.4,
     'OverallCeorating': 5,
     'Pros': 'Uptake is full of the most talented people with whom Iâve had the opportunity of working. Everyone genuinely cares about the rapid and successful growth of the company. \r\n\r\nWe have great benefits: unlimited paid time off, health/dental/vision/life, commuter benefits, gym discounts, the ability to work from home, lunch stipend Monday-Thursday and more.',
     'RatingDesc': 'Very Satisfied',
     'Recommendation': '0.8',
     'Reviewdate': '2015-12-09 13:10:32.21',
     'Senior': '3.9',
     'Website': 'www.uptake.com',
     'Work': '4.2'}




```python
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
```

    C:\Users\Nj_neeraj\Anaconda3\lib\site-packages\ipykernel\__main__.py:16: DeprecationWarning: insert is deprecated. Use insert_one or insert_many instead.
    




    ObjectId('56809be486015e3f3816f9ff')




```python
collections.find_one()
```




    {'Career': '4.2',
     'CeoName': 'Brad Keywell',
     'CeoRating': 5,
     'CeoTitle': 'CEO',
     'Compensationandbenefits': '4.3',
     'Cons': 'Weâre growing rapidly, so next steps can be unclear sometimes. We have many intelligent members of leadership who are trying to collaboratively establish our messaging, and disagreement presents challenges as we grow. I think this will work itself out over timeâweâre barely over a year old.',
     'Culturevalue': '4.0',
     'Headline': 'Really exciting opportunity.',
     'Industry': 'Computer Hardware & Software',
     'IndustryName': 'Computer Hardware & Software',
     'Location': 'Chicago, IL',
     'Name': 'Uptake',
     'No_Rating': 11,
     'OVRating': 4.4,
     'OverallCeorating': 5,
     'Pros': 'Uptake is full of the most talented people with whom Iâve had the opportunity of working. Everyone genuinely cares about the rapid and successful growth of the company. \r\n\r\nWe have great benefits: unlimited paid time off, health/dental/vision/life, commuter benefits, gym discounts, the ability to work from home, lunch stipend Monday-Thursday and more.',
     'RatingDesc': 'Very Satisfied',
     'Recommendation': '0.8',
     'Reviewdate': '2015-12-09 13:10:32.21',
     'Senior': '3.9',
     'Website': 'www.uptake.com',
     'Work': '4.2',
     '_id': ObjectId('56809be486015e3f3816f9ff')}




```python
#database stats
db.command({'dbstats': 1})
```




    {'avgObjSize': 457.6,
     'collections': 3,
     'dataFileVersion': {'major': 4, 'minor': 22},
     'dataSize': 2288.0,
     'db': 'uptake',
     'extentFreeList': {'num': 0, 'totalSize': 0},
     'fileSize': 67108864.0,
     'indexSize': 8176.0,
     'indexes': 1,
     'nsSizeMB': 16,
     'numExtents': 3,
     'objects': 5,
     'ok': 1.0,
     'storageSize': 20480.0}




```python
#collections stats
db.command({'collstats': 'uptake_glassdoor'})
```




    {'avgObjSize': 2032,
     'capped': False,
     'count': 1,
     'indexDetails': {},
     'indexSizes': {'_id_': 8176},
     'lastExtentSize': 8192.0,
     'nindexes': 1,
     'ns': 'uptake.uptake_glassdoor',
     'numExtents': 1,
     'ok': 1.0,
     'paddingFactor': 1.0,
     'paddingFactorNote': 'paddingFactor is unused and unmaintained in 3.0. It remains hard coded to 1.0 for compatibility only.',
     'size': 2032,
     'storageSize': 8192,
     'totalIndexSize': 8176,
     'userFlags': 1}




```python
list(collections.find())
```




    [{'Career': '4.2',
      'CeoName': 'Brad Keywell',
      'CeoRating': 5,
      'CeoTitle': 'CEO',
      'Compensationandbenefits': '4.3',
      'Cons': 'Weâre growing rapidly, so next steps can be unclear sometimes. We have many intelligent members of leadership who are trying to collaboratively establish our messaging, and disagreement presents challenges as we grow. I think this will work itself out over timeâweâre barely over a year old.',
      'Culturevalue': '4.0',
      'Headline': 'Really exciting opportunity.',
      'Industry': 'Computer Hardware & Software',
      'IndustryName': 'Computer Hardware & Software',
      'Location': 'Chicago, IL',
      'Name': 'Uptake',
      'No_Rating': 11,
      'OVRating': 4.4,
      'OverallCeorating': 5,
      'Pros': 'Uptake is full of the most talented people with whom Iâve had the opportunity of working. Everyone genuinely cares about the rapid and successful growth of the company. \r\n\r\nWe have great benefits: unlimited paid time off, health/dental/vision/life, commuter benefits, gym discounts, the ability to work from home, lunch stipend Monday-Thursday and more.',
      'RatingDesc': 'Very Satisfied',
      'Recommendation': '0.8',
      'Reviewdate': '2015-12-09 13:10:32.21',
      'Senior': '3.9',
      'Website': 'www.uptake.com',
      'Work': '4.2',
      '_id': ObjectId('56809be486015e3f3816f9ff')}]




```python
list(collections.find({'Name':'Uptake'}))
```




    [{'Career': '4.2',
      'CeoName': 'Brad Keywell',
      'CeoRating': 5,
      'CeoTitle': 'CEO',
      'Compensationandbenefits': '4.3',
      'Cons': 'Weâre growing rapidly, so next steps can be unclear sometimes. We have many intelligent members of leadership who are trying to collaboratively establish our messaging, and disagreement presents challenges as we grow. I think this will work itself out over timeâweâre barely over a year old.',
      'Culturevalue': '4.0',
      'Headline': 'Really exciting opportunity.',
      'Industry': 'Computer Hardware & Software',
      'IndustryName': 'Computer Hardware & Software',
      'Location': 'Chicago, IL',
      'Name': 'Uptake',
      'No_Rating': 11,
      'OVRating': 4.4,
      'OverallCeorating': 5,
      'Pros': 'Uptake is full of the most talented people with whom Iâve had the opportunity of working. Everyone genuinely cares about the rapid and successful growth of the company. \r\n\r\nWe have great benefits: unlimited paid time off, health/dental/vision/life, commuter benefits, gym discounts, the ability to work from home, lunch stipend Monday-Thursday and more.',
      'RatingDesc': 'Very Satisfied',
      'Recommendation': '0.8',
      'Reviewdate': '2015-12-09 13:10:32.21',
      'Senior': '3.9',
      'Website': 'www.uptake.com',
      'Work': '4.2',
      '_id': ObjectId('56809be486015e3f3816f9ff')}]




```python
#inserting my data(reviews, rating etc/) into database.

collections.insert([  { 'CompanyForMe': 'Great Company', 'Myreviews_WorkPlace': 'looks good from reviews'}, {'Rating':5}
                ])
```

    C:\Users\Nj_neeraj\Anaconda3\lib\site-packages\ipykernel\__main__.py:1: DeprecationWarning: insert is deprecated. Use insert_one or insert_many instead.
      if __name__ == '__main__':
    




    [ObjectId('56809e2d86015e3f3816fa00'), ObjectId('56809e2d86015e3f3816fa01')]




```python
#data object has been successfully added. (see at the bottom.)
list(collections.find())
```




    [{'Career': '4.2',
      'CeoName': 'Brad Keywell',
      'CeoRating': 5,
      'CeoTitle': 'CEO',
      'Compensationandbenefits': '4.3',
      'Cons': 'Weâre growing rapidly, so next steps can be unclear sometimes. We have many intelligent members of leadership who are trying to collaboratively establish our messaging, and disagreement presents challenges as we grow. I think this will work itself out over timeâweâre barely over a year old.',
      'Culturevalue': '4.0',
      'Headline': 'Really exciting opportunity.',
      'Industry': 'Computer Hardware & Software',
      'IndustryName': 'Computer Hardware & Software',
      'Location': 'Chicago, IL',
      'Name': 'Uptake',
      'No_Rating': 11,
      'OVRating': 4.4,
      'OverallCeorating': 5,
      'Pros': 'Uptake is full of the most talented people with whom Iâve had the opportunity of working. Everyone genuinely cares about the rapid and successful growth of the company. \r\n\r\nWe have great benefits: unlimited paid time off, health/dental/vision/life, commuter benefits, gym discounts, the ability to work from home, lunch stipend Monday-Thursday and more.',
      'RatingDesc': 'Very Satisfied',
      'Recommendation': '0.8',
      'Reviewdate': '2015-12-09 13:10:32.21',
      'Senior': '3.9',
      'Website': 'www.uptake.com',
      'Work': '4.2',
      '_id': ObjectId('56809be486015e3f3816f9ff')},
     {'CompanyForMe': 'Great Company',
      'Myreviews_WorkPlace': 'looks good from reviews',
      '_id': ObjectId('56809e2d86015e3f3816fa00')},
     {'Rating': 5, '_id': ObjectId('56809e2d86015e3f3816fa01')}]




```python

```
