import utilities
import os
import pandas as pd


file = "./datasets/archive/classical_piano.csv"

df = pd.DataFrame(columns=['n1', 'n2', 'creation_time'])
with open(file, 'r') as f:
    for row in f:
        if '<edge id' in row:
            prow = row.lstrip().replace('\n', '').split(' ')
            source = prow[2].split('=')[1].replace('"', '').split('-')
            n1 = source[0]
            n2 = prow[3].split('=')[1].replace('"', '').split('-')[0]
            creation_time = source[1]
            # print(n1, n2, creation_time)

            df.loc[len(df.index)] = [
                n1, n2, creation_time]

df.to_csv('./datasets/classical_piano.csv', index=False, sep=' ')
