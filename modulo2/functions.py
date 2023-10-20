dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

# def km_media(dataset, ano_atual):
#     for item in dataset.items():
#         result = item[1]['km'] / (ano_atual - item[1]['ano'])
#         print(result)

# print(km_media(dados, 2019))

# def km_media(dataset, ano_atual):
#     result = {}
#     for item in dataset.items():
#         media = item[1]['km'] / (ano_atual - item[1]['ano'])
#         result.update({item[0]: media})
#     return result

# print(km_media(dados, 2019))

# lista = [1,2,3,4,5,6]
# def media(array):
#     result = sum(array) / len(array)
#     return result
# resultado = media(lista)
# print(resultado)

def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({'km_media': media})
        result.update({item[0]: result})
    return result
resultado = km_media(dados, 2019)
print(resultado)