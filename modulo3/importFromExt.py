import pandas as pd

# json_file = open('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo3/files/aluguel.json')
# print(json_file.read())
# df_json = pd.read_json('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo3/files/aluguel.json')
# print(df_json)

# txt = open('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo3/files/aluguel.txt')
# print(txt.read())
# df_txt = pd.read_table('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo3/files/aluguel.txt')
# print(df_txt)

# df_xlsx = pd.read_excel('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo3/files/aluguel.xlsx')
# print(df_xlsx)

# df_html = pd.read_html('C:/Users/matheus.borges/Desktop/Estudo/OFM/Python/modulo3/files/dados_html_1.html')
# print(df_html)

df_html2 = pd.read_html('https://unafiscosaude.org.br/site/comparativo-de-planos/')
print(df_html2)