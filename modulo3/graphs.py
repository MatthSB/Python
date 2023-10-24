import pandas as pd
import matplotlib.pyplot as plt

plt.rc('figure', figsize=(15,8))
data= pd.read_csv('modulo3/files/aluguel_residencial_s_outliers.csv', sep=';')
area = plt.figure()
g1 = area.add_subplot(2,2,1)
g2 = area.add_subplot(2,2,2)
g3 = area.add_subplot(2,2,3)
g4 = area.add_subplot(2,2,4)

g1.scatter(data['Valor'], data['Area'])
g1.set_title('Valor X Area')

g2.hist(data['Valor'])
g2.set_title('Histograma')

data_g3 = data['Valor'].sample(100)
data_g3.index = range(data_g3.shape[0])
g3.plot(data_g3)
g3.set_title('Amostra (Valor)')

data_g4 = data.groupby('Tipo')['Valor']
label = data_g4.mean().index
valores = data_g4.mean().values
g4.bar(label, valores)
g4.set_title('Valor Médio por Tipo')

plt.show()

area.savefig('modulo3/files/grafico_aluguel_residencial_s_outliers.png', dpi = 300, bbox_inches = 'tight')
# print(data.head())