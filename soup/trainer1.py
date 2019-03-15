# Extracts dog_list(dog_name,link) from trainer website
# ukdogracing.net/$trainer

from bs4 import BeautifulSoup
import pprint

# read a sting from a text file
soup = BeautifulSoup(open("/home/user/bet/dogs/trainer_pclarke.html"))

dog_list = dict()

# finds all <a> tags within the selection and prints the href tag 
#table = soup.select('div[class="dog-item"]')

# trainer name currently held at this position
print soup.find('h1').text#table

for dog in soup.select('div[class="dog-item"]'):
	#for dog in table.findAll('div','dog-item'):
	dog_list[dog.a.text.strip()] =  dog.a['href']
	
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dog_list)