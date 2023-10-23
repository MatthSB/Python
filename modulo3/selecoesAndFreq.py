import pandas as pd

# data = pd.read_csv('C:/Users/mathe/OneDrive/Documentos/GitHub/Python/modulo3/files/aluguel_residencial.csv', sep=';')

# aptos = data['Tipo'] == 'Apartamento'
# data_aptos = data[aptos].shape[0]

# casas = (data['Tipo'] == 'Casa') | (data['Tipo'] == 'Casa de Condomínio') | (data['Tipo'] == 'Casa de Vila')
# data_casas = data[casas].shape[0]

# area = (data['Area'] >= 60) & (data['Area'] <= 100)
# data_area = data[area].shape[0]

# rooms_value = (data['Quartos'] >= 4) & (data['Valor'] < 2000)
# data_rooms_values = data[rooms_value].shape[0]

alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

aprovados = alunos['Aprovado'] == True
data_aprovados = alunos[aprovados]
data_aprovados.index = range(data_aprovados.shape[0])

alunas_aprov = (alunos['Sexo'] == 'F') & (alunos['Aprovado'] == True)
data_alunas_aprov = alunos[alunas_aprov]
data_alunas_aprov.index = range(data_alunas_aprov.shape[0])

idade = ((alunos['Idade'] > 10) & (alunos['Idade'] < 20) | (alunos['Idade'] >= 40))
data_idade = alunos[idade]
data_idade.index = range(data_idade.shape[0])
# df = data_idade.sort_values(by = ['Nome'])

reprovados = alunos['Aprovado'] == False
# data_reprovados = alunos[['Nome', 'Sexo', 'Idade']][reprovados]
data_reprovados = alunos.loc[reprovados, ['Nome', 'Sexo', 'Idade']]

novos = alunos.sort_values(by = ['Idade'], inplace = True)

print(novos.iloc[:3])