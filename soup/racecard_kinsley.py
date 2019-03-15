# Extract race information and dog, trainer/owner links from ukdogracing.net
from bs4 import BeautifulSoup
import pprint

# read a sting from a text file
soup = BeautifulSoup(open("/home/user/bet/dogs/racecard_kinsley.html"))

dogs = dict()

# finds all <a> tags within the selection and prints the href tag 
for table in soup.findAll('div','table-racecard-contain-item'):
	sub_table = table.find("tbody")
	title = table.find("div", {"class":"ctleft"}).text
	print title
	for row in sub_table.findAll('tr'):
		if row.a:
			odds = row.find('td','odds-td')
			trainer = row.find('td','trainer-td')
			print "race:		"+	row.div.text.strip()
			print "owner:		"+	trainer.span.text
			print "trainer:	"+	trainer.a.text.strip()+"	"+trainer.a["href"]
			print "runner:		"+	row.a.text.strip()+"	"+row.a['href']
			print "odds:		"+	odds.text.strip()
			
			#print row.td.div
#		b = row.td.div
#		print b.contents
			
			
#	for line in t.select("tr"):
	#	dog_name = 
		#print line
#		print line.find("div",{"class":"race-pos-no"})
#		print line.find("a")
#		print line.find("span")
#		print line.find("td", {"class":"trainer-td"})
#		print line.find("td", {"class":"best-td"})
		#d = dlink.find("a")
		#		best = item.find("td", {"class":"best-td"}).text
#		trainer = item.find("td", {"class":"trainer-td"}).a.text
#		tlink = item.find("td",{"class":"trainer-td"}).a['href']
#		owner = item.find("span",{"class":"new-line"}).text
		#print dlink#, trainer, tlink, owner
		
			#name = races.find()for meet in races.
		
		
			#for row in dog.find("tbody")
			
#races[dog.text.strip()] = dog
#cd print races	
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(races)	
		
# prepend domain
# wget all links to file