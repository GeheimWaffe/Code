from bs4 import BeautifulSoup
import urlgrabber

# Define the url
url = 'https://app.powerbi.com/sharedwithme/reports/f782fcc6-d2f0-4828-a81b-98d41d7852dd/ReportSection8ecdafa8076f8e9c357e'

# open the page
page = urlgrabber.urlopen(url)

# parse the Webpage
soup = BeautifulSoup(page, 'html.parser')

# print the soup
print(soup)
