import pandas as pd

data = pd.read_csv('modulo3/files/aluguel_residencial.csv', sep=';')
data['Valor Bruto'] = data['Valor'] + data['Condominio'] + data['IPTU']
data['Valor m2'] = (data['Valor'] / data['Area']).round(2)
data['Valor Bruto m2'] = (data['Valor Bruto'] / data['Area']).round(2)
casa = ['Casa', 'Casa de Condominio', 'Casa de Vila']
data['Tipo Agregado'] = data['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
# data_casa = data['Tipo'] == 'Casa'
# print(data[~data_casa].head(10))
# print(data)

# alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
#                         'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
#                         'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
#                         'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6]}, 
#                         columns = ['Nome', 'Idade', 'Sexo', 'Notas'])
# alunos['Notas-Média(Notas)'] = alunos['Notas'] \
#     .apply(lambda x: x - alunos['Notas'].mean())
# print(alunos)

data_aux = pd.DataFrame(data[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])
# print(data_aux.head(10))
del data_aux['Valor Bruto']
data_aux.pop('Valor Bruto m2')
data.drop(['Valor Bruto', 'Valor Bruto m2'], axis=1, inplace=True)
# print(data.head(10))
data.to_csv('modulo3/files/aluguel_residencial.csv', sep=';', index=False)