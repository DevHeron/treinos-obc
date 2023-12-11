from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - acessando o site

browser = webdriver.Chrome()
browser.get('https://registro.br')

# 2 - Buscando elementos
elem = browser.find_element(By.ID, 'is-avail-field')
elem.clear()
elem.send_keys('botscompython.com.br')
elem.send_keys(Keys.ENTER)
browser.save_screenshot('dominio.png')
time.sleep(5) 