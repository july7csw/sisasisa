import pandas as pd

filename = 'result_2019-2020_ver2.xlsx'
data = pd.read_excel(filename)

data_word = data.용어
data_aug = data.AUG

df = pd.DataFrame({'용어': data_word, '202008': data_aug})

df = df.sort_values(by='202008', ascending=False)
df = df.head(10)

print(df)
