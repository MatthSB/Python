import pandas as pd

dataset = pd.read_csv('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo2/files/db.csv', sep=';')

# selectMotor = dataset.Motor == 'Motor Diesel'
# selectData = dataset.Zero_km == True

# print(dataset[(selectMotor) & (selectData)])

# dataset.query('Motor == "Motor Diesel" and Zero_km == True')

# dados2 = {
#     'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor Diesel', 'Motor 1.6'],
#     'Ano': [2019, 2003, 1991, 2019, 1990],
#     'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
#     'Zero_km': [True, False, False, True, False],
#     'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
# }

# dataset2 = pd.DataFrame(dados2, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])
# print(dataset2.query('Motor == "Motor Diesel" or Motor == "Motor 4.0 Turbo"'))

# for index, row in dataset2.iter():
#   if 2019 - row['Ano'] != 0:
#     dataset2.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
#   else:
#     dataset2.loc[index, 'Km_media'] = 0

# dataset.fillna(0, inplace=True)
dataset.dropna(subset=['Quilometragem'], inplace=True)
print(dataset[dataset.Quilometragem.isna()])
# print(dataset[dataset.Quilometragem.isna()])
# print(dataset.Quilometragem)