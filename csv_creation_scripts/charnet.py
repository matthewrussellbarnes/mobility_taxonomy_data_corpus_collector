import utilities
import os
import pandas as pd


path = os.path.join(utilities.dataset_path, "archive/charnet")

for _, dirs, files in os.walk(path, topdown=True):
    for file in files:
        print(file)
        with open(os.path.join(path, file), 'r') as f:
            df = pd.DataFrame(columns=['n1', 'n2', 'creation_time'])
            for row in f:
                split_row = row.replace('\n', '').split(':')
                creation_time = split_row[0]
                split_edges = split_row[1].split(';')
                for edge in split_edges:
                    split_edge = edge.split(',')
                    if len(split_edge) == 2:
                        n1 = split_edge[0]
                        n2 = split_edge[1]
                        df.loc[len(df.index)] = [
                            n1, n2, creation_time]
                    else:
                        for n1 in split_edge:
                            for n2 in split_edge:
                                if n1 != n2:
                                    df.loc[len(df.index)] = [
                                        n1, n2, creation_time]

            df.to_csv(
                f"./datasets/{file}", index=False, sep=' ')
