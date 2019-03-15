'''
 Read program.txt, for every VENUE call the function:
	python racecard.py VENUE
 This results in a files for runners and trainers, where 
 each file is a list of links to all runners/trainers for
 every race in program.txt. 
'''
import os

# read program.txt, extract the Venue names
track = dict()
venues = []
with open("program.txt", 'r') as file:
	for line in file:
		fields = line.split(":",1)
		#track[fields[0]] = fields[1].strip()
		venues.append(fields[0])
# pass these to racecard.py, which opens the corresponding 
# racecard html file and extracts the runners
# and the trainers to files
# ----    MPI    ----
for item in venues:
	os.system("python racecard.py "+item) 
