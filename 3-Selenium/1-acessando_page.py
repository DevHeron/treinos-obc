from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# - 1 Utilizando webdriver

browser = webdriver.Chrome()
print(browser)

browser.get('http://www.amazon.com.br')

# 2 - Acessando elementos numa página

elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.send_keys('ps5')
elem.send_keys(Keys.ENTER)

#browser.quit()

