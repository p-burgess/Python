'''
 Capture dog name, birth-year, colour, sex and land for all races
 today. This will be used to uniquely identify every dog, so that
 its statistics can be compared to the other dogs in its race.

 download the racing program from the main site:

	lynx --source --accept-all-cookies http://www.ukdogracing.net/ > program.html
	
	this is used as input to this program

'''
# Extract racecard links from ukdogracing.net
from bs4 import BeautifulSoup
#import pprint
import pickle

# read a sting from a text file
soup = BeautifulSoup(open("/home/user/bet/dogs/program.html"))

#works..
#for race in soup.find_all("div", {"id" : "cardsMatrixContainer"}):
#	print race
#..

# finds all div in a soup within <div> tags 
# with class= "..racecard-item.."
races = dict()
venues = []
program = soup.find("div","racecards-contain")
for event in program.findAll("div", {"class":"racecard-item"}):
	#print event
	# find the header of the div which contains an href to the 
	# the racecard for each venue
	item = event.find("div","mini-header")
	venue = item.find("a")
	if venue != -1 and venue != None:
#		print venue.string
		venues.append(venue.string)
		races[venue.string] = "http://www.ukdogracing.net"+venue["href"]
			
# write list to a file
# format:	venue : href
with open("program.txt", 'w') as file:
	for item in venues:
		file.write('{}\n'.format(item))
	for item in races:
		file.write('{}:{}\n'.format(item,races[item]))

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(races)	
		
# wget all links to files