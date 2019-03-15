'''
 This script uses urllib to search greyhoundstats.co.uk for a
 dog, whose name is passed as a command line arguement. The response
 is saved as a file, with name runner-DOGNAME.html.
 The script results in the creation of one file and one page request.
'''
'''
import urllib
import urllib2
import sys

url = "http://greyhoundstats.co.uk/find_greyhound.php"

dogname = sys.argv[1].replace("_"," ")
values = {'name' : dogname}
print dogname

data = urllib.urlencode({'name':dogname})
results = urllib2.urlopen(url, data)

print results

filename = "runner-"+sys.argv[1]+".html"
with open(filename, 'w') as file:
	file.write(results.read())
	

data = urllib.urlencode('dogref':dogname)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req) 
webpage = response.read()

print webpage
with open("results.html", "w") as f:
    f.write(results.read())


import mechanize

dogname = sys.argv[1].replace("_"," ")
url = "http://greyhoundstats.co.uk/find_greyhound.php"
br = mechanize.Browser()
br.set_handle_robots(False) # ignore robots
br.open(url)
br.select_form(name="OF")
br["name"] = dogname
res = br.submit()
content = res.read()
with open("mechanize_results.html", "w") as f:
    f.write(content)


	
import sys	
import urllib2, urllib
url = 'http://greyhound-data.com/breed.htm'
dogname = sys.argv[1].replace("_"," ")
data = urllib.urlencode({'dogref' : dogname})
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
d = response.read()
print d

 
 
import urllib2, urllib
mydata=[('dogref','Swift Oran'),('name','OF')]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path='http://greyhoundstats.co.uk/find_greyhound.php'    #the url you want to POST to
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
page=urllib2.urlopen(req).read()
print page


import requests
userdata = {"dogref": "Swift Oran"}
resp = requests.post('http://greyhoundstats.co.uk/find_greyhound.php', params=userdata)
print resp


'''

##################################### Method 1
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('http://www.greyhound-data.com/login.htm')

# View available forms
for f in br.forms():
    print f

# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=1)

# User credentials
br.form['login'] = 'pburgess4@hotmail.com'
br.form['password'] = 'Abrighterday1'

# Login
br.submit()

print(br.open('http://www.greyhound-data.com/breed.htm').read())
