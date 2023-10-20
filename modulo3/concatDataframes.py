import pandas as pd

#LIST
data = [[1,2,3],[4,5,6],[7,8,9]]
index = ['Linha ' + str(i + 1) for i in range(3)]
columns = ['Coluna ' + str(i + 1) for i in range(3)]
df1 = pd.DataFrame(data, index, columns)
df1[df1 > 0] = 'A'
# print(df1)

#DICT
data2 = {'Coluna 1': {'Linha 1': 1,'Linha 2': 4,'Linha 3': 7},
         'Coluna 2': {'Linha 1': 2,'Linha 2': 5,'Linha 3': 8},
         'Coluna 3': {'Linha 1': 3,'Linha 2': 5,'Linha 3': 9}}
df2 = pd.DataFrame(data2)
df2[df2 > 0] = 'B'
# print(df2)

#TUPLES
data3 = [(1,2,3),(4,5,6),(7,8,9)]
index3 = ['Linha ' + str(i + 1) for i in range(3)]
columns3 = ['Coluna ' + str(i + 1) for i in range(3)]
df3 = pd.DataFrame(data3, index3, columns3)
df3[df3 > 0] = 'C'
# print(df3)

df4 = pd.concat([df1, df2, df3], axis=1)
print(df4)