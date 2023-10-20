# print(tuple([1,2,3,['nome','tupla']]))

# teste = ('Uma tupla', 1, 2)
# print(teste)
# print(type(teste))

# print((1,2,3))

# print(teste[0])
# print(teste[-1])


# for item in teste:
#   print(item)

# primeiro, segundo, terceiro = teste
# print(primeiro, segundo, terceiro)

# _,a,_ = teste
# print(a)

# b,*_ = teste
# c = teste
# print(c)
teste2 = ['a','b','c','d','e','f']
teste3 = [1,2,3,4,5,6]
# print(list(zip(teste2,teste3)))
for letra, numero in zip(teste2,teste3):
  print(letra, numero)