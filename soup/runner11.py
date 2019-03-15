'''
 This script accepts as input a dog name, it then reads
 the database file associated with that dog to calculate
 a handicap for the dog, which it saves in a text file,
 with the dog name.
 
 This information is saved in a file runner-DOGNAME.txt
 format:
	
'''

from bs4 import BeautifulSoup
import pprint
import re
import sys 
import time
