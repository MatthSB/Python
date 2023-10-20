import pandas as pd

# carros = ['Jetta Variant', 'Passat', 'CrossFox']
# print(pd.Series(carros))

# dados = [
#     {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
#     {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
#     {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
# ]

# dataset = pd.DataFrame(dados)

# print(dataset)

# print(dataset[['Nome', 'Ano', 'Valor']])

dados2 = {'Nome': ['Jetta Variant','Passat','Crossfox'], 'Motor': ['Motor 4.0 Turbo','Motor Diesel','Motor Diesel V8'],'Ano': [2003,1991,1990],
          'Quilometragem': [44410.0,5712.0,37123.0], 'Zero_km': [False,False,False], 'Valor': [88078.64,106161.94,72832.16]
          }

dataset2 = pd.DataFrame(dados2)
print(dataset2.to_dict())

# dados3 = {
#     'Crossfox': {'km': 35000, 'ano': 2005}, 
#     'DS5': {'km': 17000, 'ano': 2015}, 
#     'Fusca': {'km': 130000, 'ano': 1979}, 
#     'Jetta': {'km': 56000, 'ano': 2011}, 
#     'Passat': {'km': 62000, 'ano': 1999}
# }

# def km_media(param1, param2):
#   result = {}
#   for item in param1.items():
#     media = item[1]['km'] / (param2 - item[1]['ano'])
#     item[1].update({'km_media': media})
#     result.update({item[0]: item[1]})
#   return result

# dataset3 = pd.DataFrame(km_media(dados3, 2019)).T

# print(dataset3.head(2))
# print(dataset3[:3])
# print(dataset3.loc[['Jetta', 'DS5'], ['ano']])
# print(dataset3.iloc[[1]])

# dados = {
#     'Nome': ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'], 
#     'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
#     'Ano': [2019, 2003, 1991, 2019, 1990],
#     'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
#     'Zero_km': [True, False, False, True, False],
#     'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
# }

# dataset = pd.DataFrame(dados)
# print(dataset[['Nome','Ano','Quilometragem','Valor']][1:3])

# dados = {
#     'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
#     'Ano': [2019, 2003, 1991, 2019, 1990],
#     'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
#     'Zero_km': [True, False, False, True, False],
#     'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
# }

# dataset = pd.DataFrame(dados, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])

# print(dataset.loc[['Passat','DS5'], ['Motor','Valor']])
# print(dataset.iloc[[1,3],[0,-1]])