#driver code to start selenium 
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd 
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://housing.com/in/buy/searches/M2P1h654t5gzdrea0ll_6w68ew6j3mdrkz8m_6ne1si6hotnhbq8_3nlxhdfttdcshmss_jecnctiyiinz5rs")

def get_text(xpath):
    try:
        return driver.find_element(By.XPATH, xpath).text
    except:
        return "N/A"

def safe_print(label, xpath):
    try:
        property_data[label] = get_text(xpath)  # ← store in dict
    except Exception as e:
        property_data[label] = "N/A"

def get_by_label_th(label):
    try:
        xpath = f"//tr[th[contains(text(),'{label}')]]/td/div"
        return driver.find_element(By.XPATH, xpath).text
    except:
        return "N/A"

data = []
# for each page data record
for card in range(1,147):
    main_tab = driver.current_window_handle
    try:
        property_link = driver.find_element("xpath",f"/html/body/div[1]/div[1]/div[3]/div[2]/div[1]/div[4]/div[{card}]/div/article/div[1]/div[2]/div[1]/div[1]/div[1]/a")
    except:
        continue
    time.sleep(2)
    property_link.click()
    all_tabs = driver.window_handles
    new_tab = [tab for tab in all_tabs if tab!=main_tab][0]
    driver.switch_to.window(new_tab) 
    property_data = {}
    safe_print("Title", "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/h1/div[1]/div")
    safe_print("area name","/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/h1/div[2]")
    safe_print("Price", "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/span")
    safe_print("Area", "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div/section/div[1]/div[1]/div/div")
    safe_print("Avg Price", "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div/section/div[2]/div[1]")
    safe_print("Facing", "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div/section/div[4]/div[1]")
    safe_print("Furnishing", "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div/section/div[5]/div[1]")
    property_data["Bedrooms"] = get_by_label_th("Bedrooms")
    property_data["Bathrooms"] = get_by_label_th("Bathrooms")
    property_data["Balcony"] = get_by_label_th("Balcony")
    containers = driver.find_elements(By.XPATH, "//div[contains(@class, 'T_featureContainerStyle')]")
    for container in containers:
        label = container.find_element(By.TAG_NAME, "span").text
        score = container.find_element(By.TAG_NAME, "p").text
        property_data[label] = score  # ← store label:score pair
    data.append(property_data)  # ← append collected data
    driver.close()
    driver.switch_to.window(main_tab)
driver.quit()
pd.DataFrame(data).to_csv("property_data.csv",mode="a", index=True)  # ← save to CSV
