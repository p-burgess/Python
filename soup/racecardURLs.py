#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib
import re

r = urllib.urlopen('http://beta.racingpost.com').read()
soup = BeautifulSoup(r)

#works ..
#tags = soup.find('div', id = "cardsMatrixContainer")
#print tags
#..

#tags = soup.findAll('div', id = "cardsMatrixContainer")
#table = soup.findAll('td', {'class':"rh-cardsMatrix__course"})

# finds <a> records for racecards
#for tags in soup.findAll('div', {'id':"cardsMatrixContainer"}):
#	print(tags.findAll('a', {'class':re.compile('^hidden-sm-down.*')}))

# finds <a> records for racecards
#anchors = [td.findAll('a', {'class':re.compile('^hidden-sm-down.*')}) for td in soup.findAll('div', {'id':"cardsMatrixContainer"})]
#print anchors



tags = soup.select("body a")
print tags


#anchors = [td.findAll('a', {'class':re.compile('^hidden-sm-down.*')}) for td in soup.findAll({'id':"cardsMatrixContainer"})]
#print  anchors




#tag = soup.a

#for tags in soup.findAll('div', {'id':"cardsMatrixContainer"}):
#	print tags.get("href")



#print tags 
#print div
#print table




#listext = [t.text for t in table.findAll("a")]
#print listext
#tagslinks = tags.select('cards*')
#.find("rh-cardsMatrix__course")




#tags:
#	lobbying[item.a.get_text()] = {}

#URL = item.find(class_="button-wrapper").get_text()
#	lobbying[element.a.get_text()]["href"] = URL

#print lobbying

