'''
 Download the racecards for the track-day to a set of files. These files are used for further processing.
 
 Each link to a racecard appears on a line of the file 
 program.txt. Using lynx the URL is downloaded and saved to a file 
 with a unique name for each racecard.
 
  lynx --source --accept_all_cookies http://www.ukdogracing.net/racecards/14-03-2017/VENUE > racecard_VENUE.html

'''

from bs4 import BeautifulSoup
import pprint
import urllib

# read the track names and links from "program.txt"
track = dict()
with open("program.txt", 'r') as file:
	for line in file:
		fields = line.split(":",1)
		track[fields[0]] = fields[1].strip()

'''		
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(track)
'''

# download each URL to a file
for key,value in track.items():
	response = urllib.urlopen(value)
	webpage = response.read()
	filename = "racecard-"+key.replace(" ","_")+".html"
	with open(filename, 'w') as file:
		file.write(webpage)
