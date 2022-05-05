import utilities
import os
import pandas as pd

sub_catagories = ['financial_institution',
                  'households_', 'non_financial_institution']
for sub_cat in sub_catagories:
    path = os.path.join(utilities.dataset_path,
                        "archive/nokia_investor_correlations", sub_cat)

    df = pd.DataFrame(columns=['n1', 'n2', 'creation_time'])
    for _, dirs, files in os.walk(path, topdown=True):
        for file in files:
            print(file)
            creation_time = file[len(sub_cat):-4]
            with open(os.path.join(path, file), 'r') as f:
                for row in f:
                    split_row = row.replace('\n', '').split(',')
                    n1 = split_row[0]
                    n2 = split_row[1]

                    df.loc[len(df.index)] = [
                        n1, n2, creation_time]

    df.to_csv(
        f"./datasets/nokia_investor_correlations_{sub_cat}.csv", index=False, sep=' ')
