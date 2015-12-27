
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup
import textblob

url_to_scrape = 'http://uptake.com/'

r = requests.get(url_to_scrape, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(r.content, "lxml")

print(soup.prettify)


links = soup.find_all("a")
hrefs = []
for link in links:
    if "http" in link.get('href'):
        print(link.get('href'))
        hrefs.append(link.get('href'))


l1 = hrefs[0:3]
l2 = [hrefs[5]]
l = l1+l2
print(l)



html1 = requests.get((l[0]), headers={'User-Agent': 'Mozilla/5.0'})
s1 = BeautifulSoup(html1.content,"lxml")
#remove unwanted tags, scripts etc.
for sc1 in s1(["script", "style"]):
    sc1.extract()
text1 = s1.get_text()
list1 = text1.split(',')
#print(text1)
html2 = requests.get((l[1]), headers={'User-Agent': 'Mozilla/5.0'})
s2 = BeautifulSoup(html2.content,"lxml")
for sc2 in s2(["script", "style"]):
    sc2.extract()
text2 = s2.get_text()
list2 = text2.split(',')
#print(text2)
html3 = requests.get((l[2]), headers={'User-Agent': 'Mozilla/5.0'})
s3 = BeautifulSoup(html3.content,"lxml")
for sc3 in s3(["script", "style"]):
    sc3.extract()
text3 = s3.get_text()
list3 = text3.split(',')
#print(text3)
html4 = requests.get((l[3]), headers={'User-Agent': 'Mozilla/5.0'})
s4 = BeautifulSoup(html4.content,"lxml")
for sc4 in s4(["script", "style"]):
    sc4.extract()
text4 = s4.get_text()
#print(text4)
list4 = text4.split(',')
#print(list4)



lists = list1+list2+list3+list4
lists =' '.join(lists)
wordlist = re.sub("[^a-zA-Z]", " ", lists) #removing non-letters 


###########
## sentiment polarity check
###########

from textblob import TextBlob
# get text
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in wordlist.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
#print(text)

text = text.lower()
wiki = TextBlob(text)

r = wiki.sentiment
print(r)

#print(wiki)
#The polarity score is a float within the range [-1.0, 1.0]. 
#The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
#TextBlob uses a classifier to predict the polarity of a sentence. By default it uses the Movie-Review data set. 

#Sentiment(polarity=0.2294366777013836, subjectivity=0.4917028690263986) which shows the subjectivity is neutral infact, on 
#uptake webpage. Polarity is positive (which was expected.) 

#tokenization
wiki.words

trigram=wiki.ngrams(n=3)

bigram = wiki.ngrams(n=2)

