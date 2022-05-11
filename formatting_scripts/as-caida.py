import utilities
import os
import pandas as pd

path = os.path.join(utilities.dataset_path, "archive/as-caida")

df = pd.DataFrame(columns=['n1', 'n2', 'creation_time'])
for _, dirs, files in os.walk(path, topdown=True):
    for file in files:
        print(file)
        creation_time = file[8:-4]
        with open(os.path.join(path, file), 'r') as f:
            for _ in range(8):
                next(f)
            for row in f:
                split_row = row.replace('\n', '').split('\t')
                n1 = split_row[0]
                n2 = split_row[1]

                df.loc[len(df.index)] = [
                    n1, n2, creation_time]

df.to_csv('./datasets/as-caida.csv', index=False, sep=' ')
