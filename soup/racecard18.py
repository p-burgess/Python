'''
 Load the racecard for the track-day, extract all the dog 
 and trainer names, their links and race type to files. These
 files are used for further processing.
'''

from bs4 import BeautifulSoup
import pprint
import sys

file = "/home/user/bet/dogs/racecard-"+sys.argv[1]+".html"
soup = BeautifulSoup(open(file))

trainers = dict()
runners = dict()
all_runners = dict()
info = []
data = dict()

for race in soup.findAll('div','table-racecard-contain-item'): 
	type = race.find("div", {"class":"ctright"}).text
	info.append(type.split(',',1)[0].split()[1]) # number
	info.append(race.find("div", {"class":"ctleft"}).text.split()[0]) # time
	info.append(type.split(',',1)[1].split()[0]) # class
	info.append(type.split(',',1)[1].split()[1].split()[0]) # dist
	
	sub_table = race.find("tbody")
	for row in sub_table.findAll('tr'):
		if row.a:
			trainer = row.find('td','trainer-td')
			trainers[trainer.a.text.strip()] = "http://www.ukdogracing.net"+trainer.a["href"]
			all_runners[row.a.text.strip()] = "http://www.ukdogracing.net"+row.a['href']
	info.append(runners)
	data[info[0]] = info
	runners = {}
	info = []

'''
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(a)
pp.pprint(titles)
pp.pprint(all_runners)
pp.pprint(type)
'''
# file format:
#	NAME	:	URL
with open("runners-"+sys.argv[1]+".txt", 'w') as file:
	for item in all_runners:
		file.write('{}:{}\n'.format(item.replace(" ","_"),all_runners[item]))
with open("trainers-"+sys.argv[1]+".txt", 'w') as file:
	for item in trainers:
		file.write('{}:{}\n'.format(item.replace(" ","_"),trainers[item]))
#	#	:	time	class	dist
with open("races-"+sys.argv[1]+".txt", 'w') as file:
	for key,value in data.items():
		file.write(key+': ')
		for item in value[1:4]:
			file.write('{},'.format(item))
		file.write('\n')

print "done :"+sys.argv[1]