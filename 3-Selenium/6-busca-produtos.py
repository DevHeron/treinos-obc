from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# - 1 utilização do webdriver

browser = webdriver.Firefox()
time.sleep(2)
browser.get('https://www.amazon.com.br')
time.sleep(2)

# 2 - ACESSANDO ELEMENTO DE PESQUISA
elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.send_keys('ps5')
elem.send_keys(Keys.ENTER)
time.sleep(2)

# 3 - encontrando todos os elementos de todos os resultados
element = browser.find_element(
    By.CSS_SELECTOR,
    'div.s-main-slot.s-result-list.s-search-results.sg-row'
    )
print(element)
time.sleep(2)