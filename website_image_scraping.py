# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:06:06 2020

@author: Anna
"""
# saving the current image from a website every few seconds

import io
import requests
from PIL import Image
from datetime import datetime
import time


# function to save image
def get_image(file_path:str,url:str):
    
    # getting image using the requests library 
    try:
        image_content = requests.get(url).content
    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    # get image content and save as jpeg
    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = file_path + '.jpg'
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")
        
# image address                
url = "http://192.168.0.59/jpg/image.jpg"

# loop to save image every 2 seconds until 2030
while datetime.now().year < 2030: 
    file_name = 'Scraping/' + datetime.now().strftime("%d%m%y_%H%M%S")
    get_image(file_name, url)
    time.sleep(2)
