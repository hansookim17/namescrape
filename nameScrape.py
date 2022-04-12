import requests
from bs4 import BeautifulSoup


#obtain data
data = requests.get('https://www.thoughtco.com/most-common-us-surnames-1422656')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

databoard = soup.find('table', {'class': 'mntl-sc-block-table__table'})
tbody = databoard.find('tbody')

outfile = open('listOfLastNames.txt','w')

for tr in tbody.find_all('tr'):
    
    #FIND last name (lName)
    try:
        lName = tr.find_all('td')[1].find_all('p')[0].find_all('a')[0].text.strip()
    except:
        lName = tr.find_all('td')[1].find_all('p')[0].text.strip()
    
    lName = lName.replace('\xe9','e')
    lName = lName.replace(chr(32),'_')
    
    #WRITE last name (lName)
    outfile.write(lName)
    
    #WRITE next line
    outfile.write('\n')
    

outfile.close()