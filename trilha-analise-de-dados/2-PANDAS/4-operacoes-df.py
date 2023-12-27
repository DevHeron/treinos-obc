import pandas as pd
import matplotlib.pyplot as plt

#1-Criando Dataframe de Exemplo
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Idade':[25, 30, 35, 40, 27],
    'Cargo':['Analista', 'Gerente', 'CEO', 'Analista', 'Coordenador'],
    'Salario':[5000, 8000, 15000, 4800, 6000]
}

df = pd.DataFrame(data)
# print(df)

# 2 - visualizando primeiras linhas do df
# print(df.head(2))

# 3 - Informações sobre o DataFrame
# print(df.info())

# 4 - Estatística descritiva
# print(df.describe()) # equivalente a usar o mean() naquele pd.series usado na aula 3... (e muito mais)

# 5 - Condição sobre o dataframe (salário > 5000)
# print(df[df['Salario'] > 5000])

# 6 - Ordenação (pela idade)
# print(df.sort_values(by='Idade', ascending=False))

# 7 - Adicionando coluna calculada
# df['bonus'] = df['Salario']*0.1
# print(df)

# 8 - Agrupamento por agregação
print(df.groupby('Cargo')['Salario'].mean())

# 9 - visualização básica
df.plot(
    kind='bar',
    x='Nome',
    y='Salario',
    title='Salário dos funcionários',
    rot=45
)

plt.show()