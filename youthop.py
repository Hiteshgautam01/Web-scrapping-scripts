import csv
import re

import requests
from bs4 import BeautifulSoup

csv_file = open('web_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'Apply link', 'Website link'])

code = requests.get('https://www.youthop.com/workshops/page/1')
soup = BeautifulSoup(code.text, 'html.parser')

# article headline
article_headline = soup.find(id="main")
headline = article_headline.h1.text
headline = re.sub(r'[^\x00-\x7F]+', ' ', headline)
print(headline)

# article summary paragraph
try:
        article_para = soup.find('div', class_='article-content')  # opp paragraph
        summary = article_para.p.text
        summary = re.sub(r'[^\x00-\x7F]+', ' ', summary)
        print(summary)
except AttributeError as e:
            print(
                "OOPS paragraph")
            print(str(e))

except UnicodeEncodeError as e:
            print(
                "OOPS paragraph")
            print(str(e))        

# article apply and official link
try:
        all_link = soup.find('div', class_='application-process')  # apply now link
        _a_list = all_link.find_all('a')

        apply_link = _a_list[0].get('href')
        print(apply_link)

        web_link = _a_list[1].get('href')
        print(web_link)

except AttributeError as e:
            print(
                "OOPS link")
            print(str(e))

except UnicodeEncodeError as e:
            print(
                "OOPS link")
            print(str(e))
            
csv_writer.writerow([headline, summary, apply_link, web_link])

csv_file.close()
