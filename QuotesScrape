from bs4 import BeautifulSoup
import requests
import sys
import csv
import re

csv_file = open('quotes.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Quotes','Author'])


code = requests.get('https://www.brainyquote.com/topics/love')
soup = BeautifulSoup(code.text, 'html.parser')

for para in soup.find_all('div',class_='m-brick grid-item boxy bqQt'):
	#quotes 
	quotes = para.find('div',class_="clearfix")

	_a_list = quotes.find_all('a')
	try:	

		apply_link = _a_list[1].text
		print(apply_link)

		web_link = _a_list[2].text
		print(web_link)
	
	except IndexError as m:
		apply_link = _a_list[0].text
		print(apply_link)

		web_link = _a_list[1].text
		print(web_link)

	csv_writer.writerow([apply_link,web_link])

csv_file.close
