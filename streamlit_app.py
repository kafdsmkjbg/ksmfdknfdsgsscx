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
i = 0
while i < 1:
  name = random_char(5)
  name_2 = random_char(5)
  email = EMail()
  driver = get_driver()
  driver.set_window_size(1920, 1080)
  wait = WebDriverWait(driver, 10)
  driver.get("https://myco.io/")
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/span'))).click()
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="firstName"]'))).send_keys(name)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lastName"]'))).send_keys(name_2)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))).send_keys(email.address)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="userName"]'))).send_keys(name)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys("zxcasdqwe12!A")
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmPassword"]'))).send_keys("zxcasdqwe12!A")
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link-checkbox"]'))).click()
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register-btn"]'))).click()
  time.sleep(5)
  msg = email.wait_for_message()
  myCode = msg.body
  link = (re.findall(r'(https?://auth.myco.io?.*\?.*?)\s', myCode))[0]
  link2 = extractor.find_urls(link)[0]
  driver.get(link2)
  #time.sleep(8)
  driver.get("https://myco.io/")
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
  wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/form/div[2]/div[2]/input'))).send_keys(name)
  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/form/div[2]/div[3]/input'))).send_keys("zxcasdqwe12!A")
  wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/form/div[2]/div[4]/button'))).click()
  time.sleep(8)
  driver.get("https://myco.io/videohome?v=64e459e5a9addef12597ac3a")
  wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/div/video-js/button'))).click()
  print("done")
  time.sleep(3650)
  driver.quit()


