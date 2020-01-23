import requests
from bs4 import BeautifulSoup

url = 'http://www.earlychristianwritings.com/text/romans-kjv.html'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page,'html.parser')

print(soup.get_text())