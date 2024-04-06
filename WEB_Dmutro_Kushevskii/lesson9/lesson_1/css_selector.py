import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

a = soup.select("a")
print(a[0])

a = soup.select(".text")
print(a[0])

a = soup.select("#header")
print(a)

a = soup.select("div.tags a")
print(a[0])

href = soup.select("[href^='https://']")
print(href[0])
