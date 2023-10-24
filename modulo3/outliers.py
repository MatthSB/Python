import pandas as pd
import matplotlib.pyplot as plt

plt.rc('figure', figsize=(14,6))


data = pd.read_csv('modulo3/files/aluguel_residencial.csv', sep=';')
# data.boxplot(['Valor'])
valor = data['Valor']
# Q1 = valor.quantile(.25)
# Q3 = valor.quantile(.75)
# IIQ = Q3 - Q1
# limite_inferior = Q1 - 1.5 * IIQ
# limite_superior = Q3 + 1.5 * IIQ
# select = (valor >= limite_inferior) & (valor <= limite_superior)
# new_data = data[select]
# new_data.boxplot(['Valor'])
# data.hist(['Valor'])
# new_data.hist(['Valor'])
# data.boxplot(['Valor'], ['Tipo'])
grupo_tipo = data.groupby('Tipo')['Valor']
Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
  eh_tipo = data['Tipo'] == tipo
  eh_dentro_limite = (data['Valor'] >= limite_inferior[tipo]) & (data['Valor'] <= limite_superior[tipo])
  selection = eh_tipo & eh_dentro_limite
  dados_selected = data[selection]
  dados_new = pd.concat([dados_new, dados_selected])
dados_new.boxplot(['Valor'], ['Tipo'])
plt.show()
dados_new.to_csv('modulo3/files/aluguel_residencial_s_outliers.csv', sep=';', index=False)

'''

dados = pd.read_csv('modulo3/files/aluguel_amostra.csv', sep=';')
value = dados['Valor m2']
Q1 = value.quantile(.25)
Q3 = value.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ
print(Q1, Q3, IIQ.round(2), limite_inferior.round(2), limite_superior)

'''
