idades = [18,17,20,15,9,50]

def verifica_idade(idade):
  if idade >= 18:
    print('Idade: %d. É maior de idade.' %(idade))
  elif idade < 18:
    print('Idade: %d. É menor de idade.' %(idade))

for idade in idades:
  verifica_idade(idade)

def verifica_idade2(idades):
  for idade in idades:
    if idade >= 18:
      print('Idade2: %d. É maior de idade.' %(idade))
    elif idade < 18:
      print('Idade2: %d. É menor de idade.' %(idade))

verifica_idade2(idades)