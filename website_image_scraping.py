# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:06:06 2020

@author: Anna
"""

import io
import requests
from PIL import Image
from datetime import datetime
import time


def persist_image(file_path:str,url:str):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = file_path + '.jpg'
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")
        
        
        
url = "http://192.168.0.59/jpg/image.jpg"
datetime.now().strftime("%d%m%y_%H%M%S")


file_name = 'Scraping/' + datetime.now().strftime("%d%m%y_%H%M%S")
persist_image('Scraping/test', url)

while datetime.now().year < 2030: 
    file_name = 'Scraping/' + datetime.now().strftime("%d%m%y_%H%M%S")
    persist_image(file_name, url)
    time.sleep(2)
