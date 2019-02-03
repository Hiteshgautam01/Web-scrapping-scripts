import csv
import re

import requests
from bs4 import BeautifulSoup

csv_file = open('arma.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(
    [
        'category_href',
        'pageNo',
        'Armacad Link',
        'Title',
        'Image', 
        'Deadline',
        'Disciplines', 
        'Eligible Countries', 
        'Host Country', 
        'Study Levels', 
        'Opportunities'        
    ]
)

def pagenation(category_href):
    scrapped_links = []
    for i in range(1, 22):
        page_code = requests.get('https://armacad.info' + str(category_href) + '?order=soon&id=&page=' + str(i))
        soup = BeautifulSoup(page_code.text, 'html.parser')
        _a = None
        for para in soup.find_all('div', class_='list-cell-inner-image'):
            _a = 'https://armacad.info' + para.a.get('href')
            if _a in scrapped_links:
                return
            if _a in master_scrapped_links:
                break    
            code = requests.get(_a)
            re.compile(_a)
            soup = BeautifulSoup(code.text, 'html.parser')
            title = para.p.text

            # deadline of the opportunity
            try:
                article_deadline = soup.find('strong', class_='announcement-attr-value')
                deadline = article_deadline.text
            except AttributeError:
                deadline = '[]'

            # image of the opportunity
            article_image = soup.find('div', class_='thumbnail')
            image = 'https://armacad.info' + article_image.img.get('src')

            discipline_re = re.compile('/discipline/(.*?)">')
            discipline = discipline_re.findall(code.text)

            eligible_country_re = re.compile('/eligible-country/(.*?)">')
            eligible_country = eligible_country_re.findall(code.text)

            host_country_re = re.compile('/country/(.*?)">')
            host_country = host_country_re.findall(code.text)

            study_levels_re = re.compile('/study-level/(.*?)">')
            study_levels = study_levels_re.findall(code.text)

            opportunities_re = re.compile('<a href="/opportunities/(.*?)">')
            opportunities = opportunities_re.findall(str(soup.find_all('span', class_='announcement-attr-value')))

            # print(category_href,i,_a,title, image, deadline, discipline, eligible_country, host_country, study_levels, opportunities)
            csv_writer.writerow([category_href,i,_a,title, image, deadline, discipline, eligible_country, host_country, study_levels, opportunities])
            scrapped_links.append(_a)
            master_scrapped_links.append(_a)
            

code = requests.get('https://armacad.info/')
category_re = re.compile('<a href="(.*?)" tabindex="-1">')
category = category_re.findall(code.text)

master_scrapped_links = []
for category_href  in category:
    print(category_href)
    pagenation(category_href)
    
csv_file.close()        