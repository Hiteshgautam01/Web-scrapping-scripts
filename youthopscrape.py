from bs4 import BeautifulSoup
import requests
import sys
import csv
import re

csv_file = open('exchange programmes.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image Link','headline','summary','Website link','Deadline'])

for i in range(1,5):
	code = requests.get('https://www.youthop.com/exchange-programs/page/' + str(i))
	soup = BeautifulSoup(code.text, 'html.parser')

	for para in soup.find_all('div',class_='post-header'):
		_a = para.a.get('href')
		code = requests.get(_a)
		soup = BeautifulSoup(code.text, 'html.parser')
		
		#image of the opportunity
		try:
			article_image = soup.find('div',class_='article-media')
			image = article_image.img.get('src')
			print(image)

		except AttributeError as e:
			print("--------------------------------------------------OOPS--------------------image-----------------------------------")
			print(str(e))	

		except UnicodeEncodeError as e:
			print("--------------------------------------------------OOPS--------------------image-----------------------------------")
			print(str(e))	

		#headline of the opportunity
		try:
			article_headline = soup.find(id="main")
			headline = article_headline.h1.text
			headline = re.sub(r'[^\x00-\x7F]+',' ', headline)
			print(headline)

		except AttributeError as e:
			print("--------------------------------------------------OOPS--------------------headline-----------------------------------")
			print(str(e))	

		#short summary about the opportunity
		try:
			article_para = soup.find('div',class_='article-content') #opp paragraph
			summary = article_para.p.text
			summary = re.sub(r'[^\x00-\x7F]+',' ', summary)
			print(summary)

		except AttributeError as e:
			print("--------------------------------------------------OOPS--------------------content-----------------------------------")
			print(str(e))	

		#deadline date
		try:
			deadline_date = soup.find('ul',class_='post-details')
			date = deadline_date.li.text
			date = re.sub(r'[^\x00-\x7F]+',' ', date)
			print(date)

		except AttributeError as e:
			print("--------------------------------------------------OOPS-------------------------deadline------------------------------")
			print(str(e))	

		#Link for the official website 
		try:
			all_link = soup.find('div',class_='application-process') #apply now link
			_a_list = all_link.find_all('a')
		
			apply_link = _a_list[0].get('href')

			web_link = _a_list[1].get('href')
			print(web_link)

		except:
			IndexError as m:
			print("--------------------------------------------------OOPS-------------------------link------------------------------")
			print(str(m))

		except AttributeError as e:
			print("--------------------------------------------------OOPS-------------------------link------------------------------")
			print(str(e))	
			
		
		csv_writer.writerow([image,headline,summary,web_link,date])

csv_file.close