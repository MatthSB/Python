import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (15, 7))

dados = pd.read_csv('modulo3/files/aluguel_amostra.csv', sep = ';')
area = plt.figure()
g1 = area.add_subplot(1,2,1)
g2 = area.add_subplot(1,2,2)

grupo1 = dados.groupby('Tipo Agregado')['Valor']
labels = grupo1.count().index
valores = grupo1.count().values
g1.pie(valores, labels=labels, autopct='%1.1f%%')
g1.set_title('Total de Imóveis por Tipo Agregado')

grupo2 = dados.groupby('Tipo')['Valor']
labels = grupo2.count().index
valores = grupo2.count().values
g2.pie(valores, labels=labels, autopct='%1.1f%%', explode=(.1,.1,.1,.1,.1))
g2.set_title('Total de Imóveis por Tipo')

plt.show()