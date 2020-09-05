import requests
from bs4 import BeautifulSoup

# Requests to web server to ger HTML plain
BASE_URL = 'https://realpython.com'
response = requests.get(BASE_URL)
response_content = response.content

# BS Implementation
soup = BeautifulSoup(response_content, 'html.parser')

# print(soup)
#print(soup.title)
#print(soup.title.string)

# links = soup.find_all('a')
# print(links)
# print(len(links))

links_wrapper = soup.find('div', class_="sidebar-module sidebar-module-inset border")
# print(links_wrapper)
topics_links = links_wrapper.find_all('a', class_='badge badge-light text-muted')
# print(topics_links)
for lt in topics_links:
    print(f'{lt.text} -> {BASE_URL}{lt["href"]}')