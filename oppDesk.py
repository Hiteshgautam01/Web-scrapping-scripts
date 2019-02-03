import csv
import re
import requests
from bs4 import BeautifulSoup

oppURL = "http://www.opportunitydesk.org/2019/01/14/yali-regional-leadership-centre-southern-africa-2019/"

r = requests.get(oppURL)
soup = BeautifulSoup(r.content, 'html.parser')

img_ = soup.find('figure', class_="feat-thumb")
img = img_.a.get("href")
print (img)

title_ = soup.find('div', class_="post-title")
title = title_.h1.text
print (title)

deadline_ = re.compile('<p><strong>Deadline: (.*?)</strong></p>')
deadline = deadline_.findall(r.text)[0]
print(deadline)

cost_ = re.compile('<p><strong>Eligibility</strong></p>(.*?)<p><strong>')
cost = cost_.findall(r.text)
print(cost)

# eligibility_ = re.compile('')
# eligibility = eligibility_.search(r.content)

# application_ = re.compile('')
# application = application_.search(r.content)

# benefits_ = re.compile('')
# benefits = benefits_.search(r.content)