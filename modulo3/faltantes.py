import pandas as pd

data = pd.read_csv('modulo3/files/aluguel_residencial.csv', sep=';')
A = data.shape[0]
value_drop_null = data[data['Valor'].isnull()]
# print(value_drop_null)
data.dropna(subset = ['Valor'], inplace=True)
B = data.shape[0]
value_drop_null = data[data['Valor'].isnull()]
# print(value_drop_null)
# print(A - B)

# print(data[data['Condominio'].isnull()].shape[0])
select = (data['Tipo'] == 'Apartamento') & (data['Condominio'].isnull())
data = data[~select]
# print(data)
# print(data[data['Condominio'].isnull()].shape[0])
data = data.fillna({'Condominio': 0, 'IPTU': 0})
# print(data[data['Condominio'].isnull()].shape[0])
# print(data[data['IPTU'].isnull()].shape[0])
# print(data.info())
data.to_csv('modulo3/files/aluguel_residencial.csv', sep=';', index=False)
data2 = pd.read_csv('modulo3/files/aluguel_residencial.csv', sep=';')
# print(data2)

imoveis = pd.DataFrame([['Apartamento', None, 970, 68], 
                        ['Apartamento', 2000, 878, 112], 
                        ['Casa', 5000, None, 500], 
                        ['Apartamento', None, 1010, 170], 
                        ['Apartamento', 1500, 850, None], 
                        ['Casa', None, None, None], 
                        ['Apartamento', 2000, 878, None], 
                        ['Apartamento', 1550, None, 228], 
                        ['Apartamento', 2500, 880, 195]], 
                        columns = ['Tipo', 'Valor', 'Condominio', 'IPTU'])

imoveis.dropna(subset=['Valor'], inplace=True)
selection = (imoveis['Tipo'] == 'Apartamento') & (imoveis['Condominio'].isnull())
dados = imoveis[~selection]
dados = dados.fillna({'Condominio': 0, 'IPTU': 0})
dados.index = range(dados.shape[0])
# print(dados)

atletas = pd.DataFrame([['Marcos', 9.62], ['Pedro', None], ['João', 9.69], 
                        ['Beto', 9.72], ['Sandro', None], ['Denis', 9.69], 
                        ['Ary', None], ['Carlos', 9.74]], 
                        columns = ['Corredor', 'Melhor Tempo'])
atletas.fillna(atletas['Melhor Tempo'].mean(), inplace=True)
print(atletas)
