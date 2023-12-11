from selenium import webdriver
from selenium.webdriver.common.by import By



# - 1 Utilizando webdriver

browser = webdriver.Chrome()
print(browser)

browser.get('http://www.amazon.com.br')

browser.quit()