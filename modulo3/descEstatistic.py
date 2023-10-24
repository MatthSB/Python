import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('modulo3/files/aluguel_residencial.csv', sep=';')
bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
select = data['Bairro'].isin(bairros)
data = data[select]
data['Bairro'].drop_duplicates(inplace=True)
bairro_group = data.groupby('Bairro')
data['Valor'].mean()
# for bairro, dados in bairro_group:
#   print('{} -> {}'.format(bairro, dados['Valor'].mean()))

# print(bairro_group['Valor'].describe().round(2))
# x = bairro_group['Valor'].aggregate(['min','max']).rename(columns={'min':'Mínimo', 'max':'Máximo'})
# print(x)

# plt.rc('figure', figsize = (20,10))
# fig = bairro_group['Valor'].mean().plot.bar(color='blue')
# fig.set_ylabel('Valor do Aluguel')
# fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})
# plt.show()

'''
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])
sexo = alunos.groupby('Sexo')
sexo = pd.DataFrame(sexo['Notas'].mean().round(2))
sexo.columns = ['Notas Médias']
# print(sexo)


precos = pd.DataFrame([['Feira', 'Cebola', 2.5], 
                        ['Mercado', 'Cebola', 1.99], 
                        ['Supermercado', 'Cebola', 1.69], 
                        ['Feira', 'Tomate', 4], 
                        ['Mercado', 'Tomate', 3.29], 
                        ['Supermercado', 'Tomate', 2.99], 
                        ['Feira', 'Batata', 4.2], 
                        ['Mercado', 'Batata', 3.99], 
                        ['Supermercado', 'Batata', 3.69]], 
                        columns = ['Local', 'Produto', 'Preço'])
produtos = precos.groupby('Produto', sort=False)
# print(produtos.describe().round(2))
produtos = produtos['Preço'].aggregate(['mean','std','min','max']).round(2).rename(columns = {'mean':'Média','std':'Desvio Padrão','min': 'Mínimo','max':'Máximo'})
print(produtos)

'''

dados = pd.read_csv('modulo3/files/aluguel.csv', sep=';')
classes = [0,2,4,6,100]
labels = ['1 e 2 Quartos', '3 e 4 Quartos', '5 e 6 Quartos', '7+ Quartos']
quartos = pd.cut(dados['Quartos'], classes, labels=labels, include_lowest=True)
print(pd.value_counts(quartos))