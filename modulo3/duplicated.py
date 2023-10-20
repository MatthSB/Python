import pandas as pd
raw_data = pd.read_csv('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo3/files/aluguel.csv', sep=';')
imoveis = pd.DataFrame(raw_data.Tipo)
imoveis.drop_duplicates(inplace=True)
imoveis.columns.name = 'Id'
print(imoveis)

imoveis.index = range(1,imoveis.shape[0]+1)

print(imoveis)