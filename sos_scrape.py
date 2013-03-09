import urllib
import urllib2
from bs4 import BeautifulSoup

base = 'http://oregonvotes.org/'
stats = 'http://oregonvotes.org/pages/history/stats/'
url = 'http://oregonvotes.org/pages/history/stats/regpart.html'

# Connects to the given url, parses for the div with id='content', finds all the links in it and appends it to a given list object
def link_scrape(url,list):
	connect = urllib2.urlopen(url)
	html = connect.read()
	soup = BeautifulSoup(html)
	content = soup.find(id='content')
	links = content.find_all('a')

	# Skip the first link, which is an anchor for navigation
	for i in links[1:]:
		list.append(i.get('href'))

# Create the list before sending it to the function
years = []
# Get links to all the years the Secretary of State has available
link_scrape(url,years)

# Create the list before sending it to the function
pdfs = []

# For each year, scrape for the link to each month's pdf of voter registration numbers
for year in years:
	link_scrape(stats+year,pdfs)

# Now that we have the link to the pdf, replace the relative paths, pull out the name of the file then download it to the current directory	
for i in pdfs:
	clean = i.replace('../../..','')
	name = i.replace('../../../doc/voterresources/registration/','')
	print "Downloading %s" % name
	urllib.urlretrieve(base+clean,name)
