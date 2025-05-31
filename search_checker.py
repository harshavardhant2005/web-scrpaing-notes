from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://housing.com/")
time.sleep(2)
search_element = driver.find_element("xpath",'/html/body/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/input')
search_element.send_keys("kodungaiyur, chennai")
time.sleep(2)
search_element.send_keys(Keys.RETURN)