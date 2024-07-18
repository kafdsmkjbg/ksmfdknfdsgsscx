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


def random_char(y):
  return ''.join(random.choice(string.ascii_letters) for x in range(y))
extractor = URLExtract()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

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
wait = WebDriverWait(driver, 10)
driver.get("https://myco.io/")


