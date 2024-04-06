import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quote = soup.find("div", class_="quote")

print("Children:")
for child in quote.children:
    if child != '\n':
        print(":---------------------------------------:")
        print(child)

print(":---------------------------------------:")
print("First tag:")
first_tag = quote.find("div", class_="tags").find("a")
print(first_tag)

print(":---------------------------------------:")
print("First tag parent:")
print(first_tag.parent)

print(":---------------------------------------:")
print("First tag specific parent:")
print(first_tag.find_parent(class_="quote"))

print(":---------------------------------------:")
print("First tag siblings:")
print(f"Previous: {first_tag.find_previous_sibling('a')}")
print(f"Next: {first_tag.find_next_sibling('a')}")
