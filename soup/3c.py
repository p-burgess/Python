from bs4 import BeautifulSoup

# read a sting from a text file
soup = BeautifulSoup(open("/home/user/bet/dogs/racecards1.html"))

#works..
#for race in soup.find_all("div", {"id" : "cardsMatrixContainer"}):
#	print race
#..

# selects all elements in a soup within <div> tags with id= "..cardsMatrixContainer.."

races = dict()
for event in soup.select('div[class="racecard-item"]'):
# finds all <a> tags within the selection and prints the href tag 
	for r in event.findAll("div", {"class" : "mini-header"}):
		for r in event.findAll("a", {"class" : "left"}):
			print r
			races[r.text.strip()] = r['href']
print races		
		
# prepend domain
# wget all links to file