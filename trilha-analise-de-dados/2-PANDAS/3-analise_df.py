import pandas as pd
import pandas as pd

# - 1 Dados dos times e suas quantidades de títulos

dados_titulos = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'Liverpool': 19,
    'Juventus': 36,
    'Bayern Munich': 30
}

# 2 - Anos do título


dados_titulos = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'Liverpool': 19,
    'Juventus': 36,
    'Bayern Munich': 30
}

dados_anos = {
    'Real Madrid': [1956, 1957, 1958, 1959, 1960],
    'Barcelona':[1992, 2006, 2009, 2011, 2015],
    'Liverpool':[1977, 1978, 1981, 1984, 2005],
    'Juventus':[1958, 1985, 1996, 2011, 2015],
    'Bayern Munich':[1974, 1975, 1976, 2001, 2013]
}

# 3 - Criando a series

series_titulos = pd.Series(dados_titulos)
series_anos = pd.Series(dados_anos)

# print(series_anos)
# print(series_titulos)

# 4 - Criando dataframe combinando as series 

data = {'Títulos': series_titulos, 'Anos':series_anos}
dataframe_times = pd.DataFrame(data)
# print(dataframe_times)

# - Média de títulos
media_titulos = dataframe_times['Títulos'].mean()
print(f'Média de Títulos: {media_titulos}')

# - Time com mais títulos
mais_titulos = dataframe_times['Títulos'].idxmax()
qtd_titulos = dataframe_times['Títulos'].max()
print(f'time com mais titulos: {mais_titulos}, com {qtd_titulos} títulos')

# - Ano com mais títulos
todos_anos = (dataframe_times['Anos'].explode())
anos_mais_titulos = todos_anos.mode()[0]
print(f'ano com mais títulos: {anos_mais_titulos}')
