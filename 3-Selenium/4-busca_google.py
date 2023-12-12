from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 1 - Termo de pesquisa
term = input('Digite o que deseja pesquisar: \n')

# 2 - Iniciando driver

browser = webdriver.Firefox()
browser.get('https://www.google.com.br')
time.sleep(3)


# 3 - encontrando o elemento
elem = browser.find_element(
    By.XPATH, #xpath foi o diferencial desta aula
    "//textarea[@aria-label='Pesquisar']"
)
time.sleep(2)

# 4 - enviando termo para pesquisa
elem.send_keys(term)
elem.send_keys(Keys.ENTER)
time.sleep(2)

# 5 - quantidade de registros

results = browser.find_element(By.ID, 'result-stats').text
time.sleep(1.5)
print(f'foram encontrados {results}')

# 6 - retornando o número de páginas
frase = 'foram encontrados aproximadamente 51.600.000 resultados'
qtd_results = int(results.split('Aproximadamente ')[1].split(' resultados')[0].replace('.',''))
tot_pages = qtd_results / 10
print(f'Numero de páginas {tot_pages}')

# 7 - Navegando entre páginas
url_page = browser.find_element(
    By.XPATH,
    '//a[@aria-label="Page 2"]'.get_attrbiute('href')
)


