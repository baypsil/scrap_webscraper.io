import pdb
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

boxes=soup.find_all('div', {'class': 'col-sm-4 col-lg-4 col-md-4'})

with open('all.txt', 'w') as writer:
    for box in boxes:
        product_name = box.find('a').text
        price=box.find('h4', {'class': 'pull-right price'}).text
        description=box.find('p', {'class': 'description'}).text
        num_reviews=box.find('p', {'class': 'pull-right'}).text
        writer.write(f'{product_name} {description} {price} {num_reviews} \n')