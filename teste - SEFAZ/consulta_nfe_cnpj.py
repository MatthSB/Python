from pynfe.processamento.comunicacao import ComunicacaoSefaz

certificado = "C:/Users/matheus.borges/Documents/cert/OFM_SYSTEMS_LTDA_10771824000119_1687979049220717800.pfx"
senha = '123456'
uf = 'pr'
homologacao = True
CNPJ = '10771824000119'
# informar cnpj que deseja consultar (String) e nsu (inteiro) (por default se não informar nsu ele assumirá o valor 0, retornando as dos últimos 15 dias)

def xml_consult():
  con = ComunicacaoSefaz(uf, certificado, senha, homologacao)
  count = 0
  while count < 1:
    xml = con.consulta_distribuicao(cnpj=CNPJ, chave=None, nsu=count,
            consulta_nsu_especifico=True)
    print (xml.text)
    count += 1

xml_consult()

