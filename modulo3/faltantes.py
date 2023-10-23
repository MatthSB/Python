import pandas as pd

data = pd.read_csv('C:/Users/mathe/OneDrive/Documentos/GitHub/Python/modulo3/files/aluguel_residencial.csv', sep=';')
A = data.shape[0]
value_drop_null = data[data['Valor'].isnull()]
print(value_drop_null)
data.dropna(subset = ['Valor'], inplace=True)
B = data.shape[0]
value_drop_null = data[data['Valor'].isnull()]
print(value_drop_null)
print(A - B)
