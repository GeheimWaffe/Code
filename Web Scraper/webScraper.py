# installation de pip
from bs4 import BeautifulSoup
import urlgrabber
import csv

# define the url
urlpage = 'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

# query the website
page = urlgrabber.urlopen(urlpage)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

# find results within table
table = soup.find('table', attrs={'class':'tableSorter2'})
# print(table)
results = table.find_all('tr')
# print('Number of results', len(results))

#create and write headers to a list
rows = []

rows.append(['Rank', 'Company Name',
'Webpage', 'Description', 'Location',
'Year end', 'Annual sales rise over 3 years',
'Sales', 'Staff', 'Comments'])
# print(rows)

# sample = results[1].find_all('td')[1].find('a')['href']
# print(sample)

# loop over the results
for result in results:
    # find all columns per results
    data = result.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    else:
        rank = data[0].getText().encode('utf-8')
        company = data[1].getText().encode('utf-8')
        webpage = data[1].find('a')['href']
        location = data[2].getText().encode('utf-8')
        yearend = data[3].getText()
        salesrise = data[4].getText().encode('utf-8')
        sales = data[5].getText().encode('utf-8')
        staff = data[6].getText().encode('utf-8')
        comments = data[7].getText().encode('utf-8')

        rows.append([rank, company, webpage,
        comments, location, yearend, salesrise,
        sales, staff, comments])

# print the end results
# print(rows)

with open('techtrack100.csv', 'w') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
