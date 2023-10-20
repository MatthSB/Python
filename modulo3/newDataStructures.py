import pandas as pd

data = [1,2,3,4,5]
index = ['Linha ' + str(i + 1) for i in range(len(data))]
s = pd.Series(data, index)
print(s)

data2 = {'Linha ' + str(i + 1): i + 1 for i in range(5)}
s2 = pd.Series(data2)
print(s2)

s3 = s + s2
print(s3)