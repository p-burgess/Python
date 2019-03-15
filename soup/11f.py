	# print the names of all the owners on a page
from bs4 import BeautifulSoup

# read a sting from a text file
soup = BeautifulSoup(open("/home/user/bet/index2.html"))

# the first argument to find tells it what tag to search for
# the second you can pass a dict of attr->value pairs to filter
# results that match the first tag
table = soup.select('div[class="RC-meetingDay"]')

base_url = soup.find("a", {"title":"Racing Post Home"})
#print base_url

races=dict()

owners=list()
horses=dict()
jockeys=dict()
trainers=dict()

for card in soup.select('div[class="RC-meetingDay"]'):
	for race in card.findAll("div", {"class":"RC-meetingDay__race"}):
		time = race.find("span", {"class":"RC-meetingDay__raceTime"}).text.strip()
		#print time
		for horse in race.findAll("div", {"class":"RC-runnerCardWrapper"}):
		# make lists/dicts of all horses, owners, jockeys and
		# trainers links for lookup 
			owner_a		=horse.find("a", {"class":"RC-runnerJacket"})
			owners.append(owner_a['href'])		
			horse_a		=horse.find("a", {"class":"RC-runnerName"})
			horses[horse_a.text.strip()] = horse_a['href']		
			jockey_a	=horse.find("a", {"data-test-selector":"RC-cardPage-runnerJockey-name"})
			jockeys[jockey_a.text.strip()]=jockey_a['href']
			trainer_a	=horse.find("a", {"data-test-selector":"RC-cardPage-runnerTrainer-name"})
			trainers[trainer_a.text.strip()] = trainer_a['href']
print owners
#		print horse_a['href']
#		print jockey_a['href']
#		print trainer_a.text.strip()

#		name=hese.find("div", {"class":"RC-runnerMainWrapper"})/text()
#		name_href=hese.find("div", {"class":"RC-runnerMainWrapper"})/["href"]
#	.append()


#courselink = soup.find("a")


#table.a["href"]

#rows=list()
#for row in table.findAll("tr"):
#   rows.append(row)

# now rows contains each tr in the table (as a BeautifulSoup object)
# and you can search them to pull out the times