import pandas as pd

vendas_frutas_imported = pd.read_csv('vendas_frutas.csv')

# 1. Verificando o tipo de dados de cada coluna
print("Tipos de Dados de cada coluna:")
tipos_dados = vendas_frutas_imported.dtypes
print(tipos_dados)

# 2. Realizando a leitura de valores das colunas 'Vendas_2022' e 'Vendas_2023'
valores_vendas_2022 = vendas_frutas_imported['Vendas_2022']
valores_vendas_2023 = vendas_frutas_imported['Vendas_2023']

print("\nValores da coluna 'Vendas_2022':")
print(valores_vendas_2022)
print("\nValores da coluna 'Vendas_2023':")
print(valores_vendas_2023)

# 3. Obtendo o valor máximo das colunas 'Vendas_2022' e 'Vendas_2023'
valor_max_vendas_2022 = vendas_frutas_imported['Vendas_2022'].max()
valor_max_vendas_2023 = vendas_frutas_imported['Vendas_2023'].max()

print("\nValor máximo da coluna 'Vendas_2022':", valor_max_vendas_2022)
print("Valor máximo da coluna 'Vendas_2023':", valor_max_vendas_2023)

# 4. Verificando os dados onde a coluna 'Vendas_2022' tem valor igual a 1000
filtro_vendas_2022_1000 = vendas_frutas_imported[vendas_frutas_imported['Vendas_2022'] == 1000]

# Verificando os dados onde a coluna 'Vendas_2023' tem valor igual a 2000
filtro_vendas_2023_2000 = vendas_frutas_imported[vendas_frutas_imported['Vendas_2023'] == 2000]

print("\nDados onde 'Vendas_2022' é igual a 1000:")
print(filtro_vendas_2022_1000)

print("\nDados onde 'Vendas_2023' é igual a 2000:")
print(filtro_vendas_2023_2000)
