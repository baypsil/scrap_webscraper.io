import requests
import pandas as pd
from bs4 import BeautifulSoup
page = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/phones/touch")
soup = BeautifulSoup(page.text, features='lxml')
# import pdb; pdb.set_trace()
# print(type(soup))
# print(soup.header.p)

# soup.find_all("a", {"class" : "title"})
# # nama_produk = products[0:]
# # for product in products :
# #     print(product.text)

products = soup.find_all("a", {"title"})
nama_produk=[]
for product in products :
    nama_produk.append(product.text)
# print(nama_produk)

prices = soup.find_all("h4", {"pull-right price"})
harga=[]
for price in prices :
    harga.append(price.text)
# print(harga)

descriptions = soup.find_all("p", {"description"})
deskripsi=[]
for description in descriptions :
    deskripsi.append(description.text)
# print(deskripsi)

reviews = soup.find_all("p", {"pull-right"})
jumlah_review=[]
for review in reviews :
    jumlah_review.append(review.text)
# print(jumlah_review)

ratings = soup.find_all("div", {"ratings"})
penilaian = []
for rating in ratings :
    penilaian.append(rating.contents[3]["data-rating"])
# print(penilaian)

hasil = pd.DataFrame({
    'nama_produk': nama_produk,
    'harga' : harga,
    'deskripsi' : deskripsi,
    'jumlah_review' : jumlah_review,
    'penilaian' : penilaian
})
hasil['harga'] = hasil['harga'].str.replace('$','')
hasil['jumlah_review'] = hasil['jumlah_review'].str.replace(' reviews','')
hasil['harga'] = hasil['harga'].astype('float64')
hasil['jumlah_review'] = hasil['jumlah_review'].astype('int64')
hasil['penilaian'] = hasil['penilaian'].astype('int64')
print(hasil)
print("rata-rata harga: ", hasil['harga'].mean())
print("jumlah review: ", hasil['jumlah_review'].sum())
print("rata-rata penilaian: ", hasil['penilaian'].mean())

# with open('nama_produk.txt', 'w') as writer:
#     for product in products :
#         writer.write(f'{product.text} \n')