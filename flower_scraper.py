import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

page = requests.get('https://garden.org/plants/view/540000/Daylily-Hemerocallis-Dales-Indecision/', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.h1)
#print(page.text)
images = soup.find('img', {'class': 'thumb'})
link = images['src']
base_link = 'https://garden.org'
base_link += link
print(base_link)

flower_name = soup.h1.get_text()
flower_name = flower_name[flower_name.find("(")+1:flower_name.find(")")]
print(flower_name)

description = soup.findAll('td')

print(description[21].get_text())
