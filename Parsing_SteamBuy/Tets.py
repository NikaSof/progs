from bs4 import BeautifulSoup
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests import Session
import lxml

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}
url = "https://steambuy.com/catalog/"

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get(url = url)
main_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-item product-item_red"))) #product-item product-item_red
article = main_.find_element_by_class_name("product-item__main")
print(article)

sleep(3)
driver.close()
driver.quit()