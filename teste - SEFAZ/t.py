import requests
from zeep import Client

url = 'https://homologacao.nfe.sefa.pr.gov.br/nfe/NFeConsultaProtocolo4?wsdl'
chave_acesso = '35191041234567890123450010000012345678901234'
params = {
  'chave_acesso': chave_acesso,
  'versao': '4.00',
  'tpAmb': '2'
}

cert_path = "C:/Users/matheus.borges/Documents/cert/OFM_SYSTEMS_LTDA_10771824000119_1687979049220717800.pfx"
cert_pass = '123456'

response = requests.post(url, data=params, verify=False,
                         cert='C:/Users/matheus.borges/Documents/cert/OFM_SYSTEMS_LTDA_10771824000119_1687979049220717800.pfx')

try:
  if response.status_code == 200:
    response_xml = response.content
    client = Client(url)
    result = client.service.nfeConsultaProtocolo4(**params)
    print(result)
  else:
    print("Erro na requisição. Código Status: ", response.status_code)
except Exception as e:
  print("Erro na requisição: ", str(e))