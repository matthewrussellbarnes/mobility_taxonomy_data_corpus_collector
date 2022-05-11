import pandas as pd

file = "./datasets/archive/progamming_langaue_influence.csv"

year = {}
with open(file, 'r') as f:
    for row in f:
        prow = row.replace('\n', '').split(' ')
        if prow[0] == 'Year':
            year[prow[1].replace('"', '')] = prow[2].replace('"', '')

cite = {}
df = pd.DataFrame(columns=['n1', 'n2', 'creation_time'])
with open(file, 'r') as f:
    for row in f:
        prow = row.replace('\n', '').split(' ')
        if prow[0] == 'Cite':
            n1 = prow[1].replace('"', '')
            n2 = prow[2].replace('"', '')
            creation_time = year[prow[1].replace('"', '')]

            df.loc[len(df.index)] = [
                n1, n2, creation_time]

df.to_csv('./datasets/progamming_language_influence.csv', index=False, sep=' ')
