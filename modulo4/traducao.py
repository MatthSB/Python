import pandas as pd

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

# print(gorjetas.head())