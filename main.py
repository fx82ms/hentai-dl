import os

import bs4
import requests

def get_name(url):

    r = requests.get(url)
    b = bs4.BeautifulSoup(r.text, 'html.parser')

    name = b.find('div', id='info').h1.text

    return name

def get_images(url):

    r = requests.get(url)
    b = bs4.BeautifulSoup(r.text, 'html.parser')

    thumbnails = b.find_all('a', class_='gallerythumb')

    images = []
    for t in thumbnails:
        images.append(t.get('href'))

    return images

def get_image_src(url):

    r = requests.get('https://nhentai.net' + url)
    b = bs4.BeautifulSoup(r.text, 'html.parser')

    src = b.find('section', id="image-container").a.img['src']

    return src

def download_images(images, folder_name):

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for image in images:

        image_url      = get_image_src(image)
        image_filename = image_url.split('/')[-1]

        r = requests.get(image_url)

        if r.status_code == 200:
            with open('{}/{}'.format(folder_name, image_filename), 'wb') as f:
                f.write(r.content)

imagenes = get_images('https://nhentai.net/g/177978/')
download_images(imagenes, 'ou-sama appli')
