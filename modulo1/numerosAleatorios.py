from random import randrange, seed

print(randrange(0, 11))

notas = []
numero = 0
seed(numero)
# numero += 1
for nota in range(8):
  notas.append(randrange(0,11))

print(notas)
print(len(notas))

