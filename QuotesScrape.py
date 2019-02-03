import csv

import requests
from bs4 import BeautifulSoup

URL = 'https://www.brainyquote.com/topics/love'

# Open a csv file in write mode
csv_file = open('quotes.csv', 'w')

csv_writer = csv.writer(csv_file)
# Add Heading as first row google
csv_writer.writerow(['Quotes', 'Author'])

code = requests.get(URL)
soup = BeautifulSoup(code.text, 'html.parser')

# Find all elements with given classes
for para in soup.find_all('div', class_='m-brick grid-item boxy bqQt'):
    # Extracted Quotes
    quotes = para.find('div', class_="clearfix")

    # Find all <a> tags in the body of webpage
    _a_list = quotes.find_all('a')
    try:
        # Extract link of anchor tag of quote
        apply_link = _a_list[1].text
        print(apply_link)

        # Extract link of anchor tag of author
        web_link = _a_list[2].text
        print(web_link)

    except IndexError as m:
        apply_link = _a_list[0].text
        print(apply_link)

        web_link = _a_list[1].text
        print(web_link)

    # Write row to csv file
    csv_writer.writerow([apply_link, web_link])

csv_file.close()
