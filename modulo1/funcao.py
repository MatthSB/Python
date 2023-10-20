def saudacao():
  nome_pessoa = input('Qual seu nome? ')
  print(f'Olá, {nome_pessoa}!')
  idade_pessoa = input('Informe sua idade: ')
  print(f'Seu nome é {nome_pessoa} e você tem {idade_pessoa} anos.')

saudacao()

def saudacao_com_parametros(nome, idade):
  print(f'Olá, {nome}. Idade informada: {idade}')

saudacao_com_parametros(nome='Carlos', idade=35)
saudacao_com_parametros('Matheus', 18)