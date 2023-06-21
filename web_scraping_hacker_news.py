#!/usr/bin/env python
# coding: utf-8

# In[10]:



#pip install requests
# pip install BeautifulSoup4


# In[172]:


import requests
from bs4 import BeautifulSoup as bs
response=requests.get('https://news.ycombinator.com/news')
print(response) #<Response [200]>
# print(response.text) #gives entire html response of the site, we need to crawl this data using bs4
soup=bs(response.text,'html.parser')
# print(soup.prettify())
# soup.title  #<title>Hacker News</title>
link=soup.select('.titleline > a')
# print(link)
score=soup.select('.score')
print(type(score))
# print(score)
# for i in score:
#     only_score=i.getText().replace('points','')
#     print(only_score)
#     print(type(only_score))

def sort_func(lis):
    lis=sorted(lis, key= lambda k:k['score'], reverse=True) # this will sort the list of dic in desc order based on score
    print('--------List of top news from hacker rank based on scores------')
    print('')
    for dic in lis:
        for val in dic.values():
            print(val)

            
            
        



def filter_func(link,score):
    lis=[]
    print(type(lis))
    for ids,(item1,item2) in enumerate(zip(link,score)):
        text=item1.getText()
        href=item1.get('href')
        scores=int(item2.getText().replace('points',''))
#         print(scores)
        lis.append({'title':text,'link':href,'score':scores})
    return sort_func(lis)


filter_func(link,score)


        





        
        
filter_func(link,score)

