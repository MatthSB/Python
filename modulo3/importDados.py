# IMPORTANDO A BASE DE DADOS

import pandas as pd

data = pd.read_csv('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo3/files/aluguel.csv', sep = ';')

# INFORMAÇÕES GERAIS SOBRE A BASE DE DADOS

data_types = pd.DataFrame(data.dtypes, columns = ['Tipos de Dados'])
data_types.columns.name = 'Variáveis'
rows_and_variables = data.shape

print(data.head())