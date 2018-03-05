from bs4 import BeautifulSoup
import requests
import sys
import csv
import re

csv_file = open('web_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','Apply link','Website link'])

for i in range(1,7):
	code = requests.get('https://www.youthop.com/workshops/page/' + str(i))
	soup = BeautifulSoup(code.text, 'html.parser')
	for para in soup.find_all('div',class_='post-header'):
		_a = para.a.get('href')
		code = requests.get(_a)
		soup = BeautifulSoup(code.text, 'html.parser')
		
		#article headline
		article_headline = soup.find(id="main")
		headline = article_headline.h1.text
		headline = re.sub(r'[^\x00-\x7F]+',' ', headline)
		print(headline)

		#arcticle summary paragraph
		article_para = soup.find('div',class_='article-content') #opp paragraph
		summary = article_para.p.text
		summary = re.sub(r'[^\x00-\x7F]+',' ', summary)
		print(summary)

		#article apply and official link
		all_link = soup.find('div',class_='application-process') #apply now link
		_a_list = all_link.find_all('a')
		
		apply_link = _a_list[0].get('href')
		print(apply_link)

		web_link = _a_list[1].get('href')
		print(web_link)
			
		csv_writer.writerow([headline,summary,apply_link,web_link])


csv_file.close
