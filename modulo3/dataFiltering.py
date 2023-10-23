import pandas as pd

data = pd.read_csv('C:/Users/mathe/OneDrive/Documentos/GitHub/Python/modulo3/files/aluguel.csv', sep=';')

list(data['Tipo'].drop_duplicates())
residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']
select = data['Tipo'].isin(residencial)
dataResidencial = data[select]
dataResidencial.index = range(dataResidencial.shape[0])
# print(dataResidencial)

# numeros = [i for i in range(11)]
# letras = [chr(i + 65) for i in range(11)]
# nome_coluna = ['N']
# df = pd.DataFrame(data = numeros, index = letras, columns = nome_coluna)
# selecao = df['N'].isin([i for i in range(11) if i % 2 == 0])
# df = df[selecao]
# # print(df)

# #DATA EXPORT
dataResidencial.to_csv('C:/Users/mathe/OneDrive/Documentos/GitHub/Python/modulo3/files/aluguel_residencial.csv', sep=';', index=False)

dataResidencial2 = pd.read_csv('C:/Users/mathe/OneDrive/Documentos/GitHub/Python/modulo3/files/aluguel_residencial.csv', sep=';')

print(dataResidencial2)

#sort_index e sort_values para ordenar