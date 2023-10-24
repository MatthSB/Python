import pandas as pd
s = pd.Series(list('asdasdadadea'))
# print(s.unique())
# print(s.value_counts())

data = pd.read_csv('modulo3/files/aluguel.csv', sep=';')
# print(data['Tipo'].unique())
# print(data['Tipo'].value_counts())

m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'

eventos = {'m1': list(m1), 'm2': list(m2), 'm3': list(m3), 'm4': list(m4), 'm5': list(m5)}
moedas = pd.DataFrame(eventos)
df = pd.DataFrame(['Cara','Coroa'], ['c','C'], ['Faces'])
for item in moedas:
  df = pd.concat([df, moedas[item].value_counts()], axis=1)
print(df)