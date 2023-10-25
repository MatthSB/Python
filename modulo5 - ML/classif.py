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
treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1,1,1,0,0,0]

model = LinearSVC()
print(model.fit(treino_x, treino_y))

animal_misterioso = [1,1,1]
animal_misterioso2 = [1,0,1]
animal_misterioso3 = [1,1,0]
animal_misterioso4 = [0,1,1]

teste_x = [animal_misterioso, animal_misterioso2, animal_misterioso3, animal_misterioso4]
teste_y = [0,0,1,1]

previsoes = model.predict(teste_x)

corretos = (previsoes == teste_y).sum()
total = len(teste_x)
taxa_acertos = (corretos / total * 100).round(2)
print(taxa_acertos)
taxa_acertos = (accuracy_score(teste_y, previsoes) * 100).round(2)
print(taxa_acertos)

