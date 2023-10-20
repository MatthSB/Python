# dados = {'dado1': 1, 'dado2': 2}
# print(dados)

# teste2 = ['a','b','c','d','e','f']
# teste3 = [1,2,3,4,5,6]

# dados2 = dict(zip(teste2, teste3))
# print(dados2)
# del dados2['f']
# print(dados2)
# dados2.update({'g': 7})
# print(dados2)
# dados3 = dados2
# print(dados3)
# del dados3['g']
# print(dados2)
# print(dados3)
# dados4 = dados2.copy()
# dados4.update({'h': 8})
# print(dados2)
# print(dados4)
# print(dados4.pop('p', 'Dado não encontrado'))
# # del dados4['p']
# dados4.clear()
# print(dados4)

# print(dados.items())
# print(dados.keys())
# print(dados.values())

dados = {
    'Crossfox': {'valor': 72000, 'ano': 2005}, 
    'DS5': {'valor': 125000, 'ano': 2015}, 
    'Fusca': {'valor': 150000, 'ano': 1976}, 
    'Jetta': {'valor': 88000, 'ano': 2010}, 
    'Passat': {'valor': 106000, 'ano': 1998}
}

for item in dados.items():
  if item[1]['ano'] >= 2000:
    print(item[0])