def verifica_permissao_sem_parametro():
  # idade = int(input('Qual sua idade: ')) -> funciona
  idade = input('Qual sua idade: ')
  idade = int(idade)
  if idade >= 18:
    print(f'Você é maior de idade.')
  else:
    print(f'Você é menor de idade.')

verifica_permissao_sem_parametro()