idade = 22

def verifica_permissao(idade):
  if idade >= 18:
    print(f'É maior de idade.')
  else:
    print(f'É menor de idade.')

verifica_permissao(idade)
verifica_permissao(idade=17)