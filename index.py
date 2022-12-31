import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title)
class_name = "gem-c-document-list__item-title"
titres = soup.find_all("a", class_=class_name)
print(titres)
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
print(descriptions)