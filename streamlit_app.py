import streamlit as st
from tempmail import EMail
from urlextract import URLExtract
import time
import re
import random
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyimgur


def random_char(y):
  return ''.join(random.choice(string.ascii_letters) for x in range(y))
extractor = URLExtract()
"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    name = random_char(5)
    name_2 = random_char(5)
    email = EMail()
    driver = get_driver()
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 30)
    driver.get("https://myco.io/")
    driver.save_screenshot("screenie.png")
    CLIENT_ID = 'a030a75ec41c15d'
    def upload_image_to_imgur(image_path):
      # Authenticate with Imgur
      im = pyimgur.Imgur(CLIENT_ID)
  
      # Upload image
      uploaded_image = im.upload_image(image_path, title="Uploaded with PyImgur")
  
      # Return the direct link to the uploaded image
      return uploaded_image.link


    image_path = 'screenie.png'
    
    # Upload image and get URL
    image_url = upload_image_to_imgur(image_path)
    
    # Print the URL
    print(f"Uploaded image URL: {image_url}")
