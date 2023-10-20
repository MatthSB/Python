import matplotlib.pyplot as plt
from random import randrange, seed

'''

x = list(range(1,9))
notas = []
seed(3)
for nota in range(8):
  notas.append(randrange(0,9))

plt.plot(x, notas, marker = 'o')
plt.title('Notas de Matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
print(notas)
plt.show()

'''

notas_matematica = ['Matemática',8,7,6,6,7,7,8,10]
notas_portugues = ['Português',9,9,9,8,5,6,8,5]
notas_geografia = ['Geografia',10,10,6,7,7,7,8,7]

notas = [notas_matematica, notas_portugues, notas_geografia]

for nota in notas:
  x = list(range(1,9))
  y = nota[1:]
  plt.plot(x, y, marker = 'o')
  plt.title(nota[0])
  plt.xlabel('Provas')
  plt.ylabel('Notas')
  plt.show()
