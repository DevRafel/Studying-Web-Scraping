from bs4 import BeautifulSoup
import requests

user_agent = '@'
headers = {'User-Agent': user_agent}
url = 'https://www.vivadecora.com.br/decoracao/casa'

page = requests.get(url, headers=headers)

html = page.text

print(f'Status da Requisição: {page.status_code}')

soup = BeautifulSoup(html, 'html.parser')

soup.find_all('header', attrs={'class': 'description-box__header__title'})


print(soup)
