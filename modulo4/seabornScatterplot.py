import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#PEGANDO DADOS DA AULA ANTERIOR

data = pd.read_csv('modulo4/files/tips.csv', sep=',')

rename = {'total_bill': 'valor_da_conta', 'tip': 'gorjeta', 'dessert': 'sobremesa', 'day': 'dia_da_semana', 'time': 'hora_do_dia',
          'size': 'total_de_pessoas'}
gorjetas = data.rename(columns=rename)

sim_nao = {'No' : 'Não', 'Yes': 'Sim'}
gorjetas['sobremesa'] = gorjetas['sobremesa'].map(sim_nao)

dias = {'Sun' : 'Domingo', 'Sat': 'Sábado', 'Thur': 'Quinta', 'Fri': 'Sexta'}
gorjetas['dia_da_semana'] = gorjetas['dia_da_semana'].map(dias)

hora = {'Dinner': 'Jantar', 'Lunch': 'Almoço'}
gorjetas['hora_do_dia'] = gorjetas['hora_do_dia'].map(hora)

#VALOR DA CONTA E GORJETA
# valor_gorjeta = sns.scatterplot(gorjetas,x='valor_da_conta', y='gorjeta')
''' visualmente, o valor da gorjeta umenta conforme o valor da conta '''
# print('A base de dados contém {} registros.\n'.format(gorjetas.shape[0]))
# print('Registros não nulos')
# print(gorjetas.count())
# plt.show()

#CRIANDO CAMPO PORCENTAGEM
gorjetas['porcentagem'] = (gorjetas['gorjeta'] / gorjetas['valor_da_conta']).round(2)
# porcentagem_conta = sns.scatterplot(gorjetas, x='valor_da_conta', y='porcentagem')
''' visualmente, o valor da conta não é proporcional ao valor da gorjeta '''
# print(gorjetas.head())
# plt.show()

#RELPLOT E LMPLOT
# porcentagem_conta_linha = sns.relplot(gorjetas, x='valor_da_conta', y='porcentagem', kind='line')
# plt.show()
# porcentagem_conta_linha_1 = sns.lmplot(gorjetas, x='valor_da_conta', y='porcentagem')
# plt.show()

print(gorjetas[gorjetas['sobremesa'] == 'Sim'].describe().round(2))
print(gorjetas[gorjetas['sobremesa'] == 'Não'].describe().round(2))