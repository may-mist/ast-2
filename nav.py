import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get('https://www.google.com')
title = driver.title
print('Page Title:', title)

time.sleep(2)
driver.get('https://www.selenium.com')
time.sleep(4)
print('Page Title:', driver.title)

driver.quit()