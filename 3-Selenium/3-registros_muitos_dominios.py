from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Utilizando o webdriver

browser = webdriver.Firefox()
browser.get('http://registro.br')
time.sleep(2)

# 2 - Lista de domínios

domains = [
    'bootscompython.com.br',
    'meta.com',
    'databot.com',
    'pythonbootcamp.com',
]

file = open('domains.txt', 'w', encoding='utf-8')

# 3 - manipulando elementos

for domain in domains:
    elem = browser.find_element(By.ID, 'is-avail-field')
    elem.clear()
    elem.send_keys(domain)
    elem.send_keys(Keys.ENTER)
    time.sleep(5)

# 4 - buscando informações

    results = browser.find_elements(By.TAG_NAME, 'strong')
    text = f'Domínio {results[1].text} está {results[2].text}\n'
    print(text)
    file.write(text)

file.close
browser.close()