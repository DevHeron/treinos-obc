"""
Funcionalidades da Series:
1 - Armazenamento de Dados Unidimensionais
2 - Utilizado em operações Vetorizada
3 - Focado em Estrutura de Dados
"""

import pandas as pd

# - 1 Dados dos times e suas quantidades de títulos

dados = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'Liverpool': 19,
    'Juventus': 36,
    'Bayern Munich': 30
}

# 2 - criando serie a partir de dicionário

series_times = pd.Series(dados)
# print(series_times)
# print(type(series_times))

# 3 - Selecionar time por índice

#print(series_times['Juventss'])
#print(series_times.iloc[2])

# 4 - Selecionando por fatiamento
#print(series_times['Barcelona': 'Juventus']) # inclusivo

# 5 - Selecionando por condição
print('\n')
print(series_times[series_times > 30])

