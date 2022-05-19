from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.avito.ma/fr/maroc/informatique_et_multimedia-%C3%A0_vendre').text

soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find_all('span', class_='oan6tk-17 ewuNqy')
for article in articles:
    print (article.text)

#print(articles)
