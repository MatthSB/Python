import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 10)
# pd.set_option('display.max_columns', 10)
dataset = pd.read_csv('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo2/files/db.csv', sep = ';', index_col= 0)
print(dataset)
# print(dataset.dtypes)
# print(dataset.info())
# print(dataset[['Quilometragem', 'Valor']].describe())