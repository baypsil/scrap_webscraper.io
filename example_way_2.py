import requests
from bs4 import BeautifulSoup
 
page = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones/touch')
soup = BeautifulSoup(page.content, 'lxml')

containers = soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
# print(containers)

with open('result.txt', 'w') as writer:
  for container in containers:
    name = container.find('a',class_='title').text
    deskripsi = container.find('p',class_='description').text
    price = container.find('h4',class_='pull-right price').text
    writer.write(f'name: {name} deskprisi: {deskripsi} price:{price} \n')
