import requests
from bs4 import BeautifulSoup
from PIL import Image
from urls2 import url

print(url)
base = BeautifulSoup(requests.get(url).text)
baselist = base.find(
    'ul', class_='ve-cat-widget-listing').find_all('a', href=True)

for cada in baselist:
    print(cada['href'], cada.text)
    url_cat = cada['href']
    cate = BeautifulSoup(requests.get(url_cat).text)
    num = cate.find('span', class_='pages').text.split(' ')[-1]
    for i in range(1, 2):
        url_temp = url_cat + '/page/'+str(i)
        catPage = BeautifulSoup(requests.get(url_temp).text)
        lista = catPage.findAll('article', class_='grid_4 postlistbox')
        for each in lista:
            image_url = each.find('img')['src']
            img = Image.open(requests.get(image_url, stream=True).raw)
            img.save(image_url.split('/')[-1])
            print(image_url)
