from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.processamento.serializacao import SerializacaoXML
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.notafiscal import NotaFiscal
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.utils.flags import CODIGO_BRASIL
from decimal import Decimal
import datetime

certificado = 'C:/Users/matheus.borges/Documents/cert/OFM_SYSTEMS_LTDA_10771824000119_1687979049220717800.pfx'
senha = '123456'
uf = 'pr'
homologacao = True

#emitente
emitente = Emitente(
  razao_social = 'OFM SYSTEMS LTDA',
  nome_fantasia = 'OFM SYSTEMS LTDA',
  cnpj = '10771824000119',
  codigo_de_regime_tributario = '1',
  inscricao_estadual = '248595601',
  inscricao_municipal = '12345',
  cnae_fiscal = '9999999',
  endereco_logradouro = 'Rua Principal',
  endereco_numero = '254',
  endereco_bairro = 'Vila Mota',
  endereco_municipio = 'Adrianópolis',
  endereco_uf = 'PR',
  endereco_cep = '83490971',
  endereco_pais = CODIGO_BRASIL
)

#cliente
cliente = Cliente(
    razao_social = 'FAN FACULDADE DE ADMINISTRACAO E NEGOCIOS LTDA',
    tipo_documento = 'CNPJ',
    email = 'teste@gmail.com',
    numero_documento = '10771817000117',
    indicador_ie = 9,                                  # 9=Não contribuinte 
    endereco_logradouro = 'Rua Barão de Jaraguá',
    endereco_numero = '254',
    endereco_complemento = '',
    endereco_bairro = 'Jaraguá',
    endereco_municipio = 'Maceió',
    endereco_uf = 'AL',
    endereco_cep = '57022140',
    endereco_pais = CODIGO_BRASIL,
    endereco_telefone = '1150962910',
)

#nota fiscal
nota_fiscal = NotaFiscal(
   emitente = emitente,
   cliente = cliente,
   uf = uf.upper(),
   natureza_operacao = 'VENDA', # venda, compra, transferência, devolução, etc
   forma_pagamento = 0,         # 0 = Pagamento à vista; 1 = Pagamento a prazo; 2 = Outros.
   tipo_pagamento = 1,
   modelo = 55,                 # 55 = NF-e; 65 = NFC-e
   serie = '1',
   numero_nf = '111',           # Número do Documento Fiscal.
   data_emissao = datetime.datetime.now(),
   data_saida_entrada = datetime.datetime.now(),
   tipo_documento = 1,          # 0 = entrada; 1 = saida
   municipio = '4118402',       # Código IBGE do Município 
   tipo_impressao_danfe = 1,    # 0 = Sem geração de DANFE;1 = DANFE normal, Retrato;2 = DANFE normal Paisagem;3 = DANFE Simplificado;4 = DANFE NFC-e;
   forma_emissao = '1',         # 1 = Emissão normal (não em contingência);
   cliente_final = 1,           # 0 = Normal;1 = Consumidor final;
   indicador_destino = 1,
   indicador_presencial = 1,
   finalidade_emissao = '1',    # 1 = NF-e normal;2 = NF-e complementar;3 = NF-e de ajuste;4 = Devolução de mercadoria.
   processo_emissao = '0',      #0 = Emissão de NF-e com aplicativo do contribuinte;
   transporte_modalidade_frete = 1,
   informacoes_adicionais_interesse_fisco = 'Mensagem complementar',
   totais_tributos_aproximado = Decimal('21.06'),
)

# Produto
nota_fiscal.adicionar_produto_servico(
    codigo = '000328',                           # id do produto
    descricao = 'NOTA FISCAL EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL',
    ncm = '99999999',
    #cest = '0100100',                            # NT2015/003
    cfop = '5102',
    unidade_comercial = 'UN',
    ean = 'SEM GTIN',
    ean_tributavel = 'SEM GTIN',
    quantidade_comercial = Decimal('12'),        # 12 unidades
    valor_unitario_comercial = Decimal('9.75'),  # preço unitário
    valor_total_bruto = Decimal('117.00'),       # preço total
    unidade_tributavel = 'UN',
    quantidade_tributavel = Decimal('12'),
    valor_unitario_tributavel = Decimal('9.75'),
    ind_total = 1,
    # numero_pedido = '12345',                   # xPed
    # numero_item = '123456',                    # nItemPed
    icms_modalidade = '102',
    icms_origem = 0,
    icms_csosn = '400',
    pis_modalidade = '07',
    cofins_modalidade = '07',
    valor_tributos_aprox = '21.06'
)

# responsável técnico
nota_fiscal.adicionar_responsavel_tecnico(
    cnpj = '99999999000199',
    contato = 'SquadGemius',
    email = 'squadgemius@gmail.com',
    fone = '11912341234'
)

# serialização
serializador = SerializacaoXML(_fonte_dados, homologacao=homologacao)
nfe = serializador.exportar()

# assinatura
a1 = AssinaturaA1(certificado, senha)
xml = a1.assinar(nfe)

# envio
con = ComunicacaoSefaz(uf, certificado, senha, homologacao)
envio = con.autorizacao(modelo = 'nfe', nota_fiscal=xml)

# em caso de sucesso o retorno será o xml autorizado
# Ps: no modo sincrono, o retorno será o xml completo (<nfeProc> = <NFe> + <protNFe>)
# no modo async é preciso montar o nfeProc, juntando o retorno com a NFe  
from lxml import etree
if envio[0] == 0:
  print('Sucesso!')
  print(etree.tostring(envio[1], encoding = "unicode").replace('\n','').replace('ns0:','').replace(':ns0', ''))
# em caso de erro o retorno será o xml de resposta da SEFAZ + NF-e enviada
else:
  print('Erro:')
  print(envio[1].text) # resposta
  print('Nota:')
  print(etree.tostring(envio[2], encoding = "unicode")) # nfe