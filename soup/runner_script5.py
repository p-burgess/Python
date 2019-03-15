'''
 This script reads program.txt, and extracts all the
 name of the VENUEs. for each VENUE it will read the
 corresponding runners-VENUE.txt. These files contain
 the names of all the runners for the day. For every 
 runner, this process then checks;
 
 1. is there a file, if not it creates one
 2. is the file up to date, if not it queries the database
	for information about the dog, and updates the file
	
 This is then feed into runner.py, which computes a 
 handicap for the dog and save that to a file named analysis-DOGNAME.txt.
 
 This results in a text file for each runner for all
 racecards.
'''

import pprint
import os
import time

start_time = time.time()

track = dict()
runner = dict()

# read program.txt, extract the Venue names into a dict()
with open("program.txt", 'r') as file:
	for line in file:
		fields = line.split(":",1)
		track[fields[0]] = fields[1]

# read all runner files, extract the names into a dict()
# ----    MPI    ----
for key,value in track.items():
	filename =  "runners-"+key+".txt"
	#print filename
	with open(filename, 'r') as file:
		for line in file:
			fields = line.split(":",1)
			runner[fields[0]] = fields[1]

# ----           ----

# check if the database file exits, if not create one using
# a template
template ="#sex:dob:colour:sire:dam\n\n#date:stadium:race:class:distance:#dogs:trap:stime:finish:comment:SP:weight:time:s-time"
for key,value in runner.items():
	filename = "/home/user/bet/dogs/runner-"+key+".txt"
	if os.path.isfile(filename):
		print("file exists for:"+key)
	else:
		with open(filename,"w") as file:
			file.write(template)

# read the runner file, determine if the dogs last results
# are recent.
with open(filename,"w") as file:
	file.read(template)

	
'''
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(runners)
'''			

'''
# ----    MPI    ----
for key,value in runners.items():
	response = urllib.urlopen(value)
	webpage = response.read()
	filename = "runner-"+key+".html"
	with open(filename, 'w') as file:
		file.write(webpage)
		print "downloaded: "+key
# ----           ----

# ----    MPI    ----
for key,value in runner.items():
	os.system("python runner.py "+key) 
# ----           ----
'''
	
print "execution time :	%s" % (time.time() - start_time)	
