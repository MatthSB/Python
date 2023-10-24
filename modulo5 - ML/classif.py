from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

'''
-> features (0 => Não, 1 => Sim)
    1. pelo longo?
    2. perna curta?
    3. late?
'''
porco1 = [0,1,0]
porco2 = [0,1,1]
porco3 = [1,1,0]

cachorro1 = [0,1,1]
cachorro2 = [1,0,1]
cachorro3 = [1,1,1]

# 1 => Porco, 0 => Cachorro
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
classes = [1,1,1,0,0,0]

model = LinearSVC()
print(model.fit(dados, classes))

animal_misterioso = [1,1,1]
animal_misterioso2 = [1,0,1]
animal_misterioso3 = [1,1,0]
animal_misterioso4 = [0,1,1]

testes = [animal_misterioso, animal_misterioso2, animal_misterioso3, animal_misterioso4]
previsoes = model.predict(testes)
testes_classes = [0,0,1,1]

taxa_acertos = accuracy_score(testes_classes, previsoes) * 100

print(taxa_acertos)