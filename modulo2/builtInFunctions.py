dados = {'valor1': 1, 'valor2': 2, 'valor3': 3, 'valor4': 4}
# valores = []

# for valor in dados.values():
#   valores.append(valor)
# print(valores)

valores = list(dados.values())

# soma = 0
# for valor in dados.values():
#   soma += valor
# print(soma)

somaValores = sum(dados.values())
print(somaValores)