import pandas as pd

#1-Criando Dataframe de Exemplo
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Idade':[25, 30, 35, 40, 27],
    'Cargo':['Analista', 'Gerente', 'CEO', 'Analista', 'Coordenador'],
    'Salario':[5000, 8000, 15000, 4800, 6000]
}

df = pd.DataFrame(data)
print(df)