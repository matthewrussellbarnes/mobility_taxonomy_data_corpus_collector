import os
import pandas as pd

import utilities


def format_dataset(extracted_fpath):
    if not extracted_fpath:
        return

    delimiter = ' '
    fname = 'reuters_terror_news.csv'

    col_no = 4
    n1_no = 0
    n2_no = 1
    ct_no = 3
    print(extracted_fpath, 'formatting')

    columns = ['n1', 'n2', 'creation_time']

    names = [None] * col_no
    names[n1_no] = columns[0]
    names[n2_no] = columns[1]
    names[ct_no] = columns[2]

    try:
        fdf = pd.read_csv(extracted_fpath, names=names,
                          delimiter=delimiter, skipinitialspace=True, skiprows=13311)
    except Exception as e:
        print(e, '\n')
        return

    fdf[columns[2]] = [ct.replace('[', '').replace(']', '')
                       for ct in fdf[columns[2]]]
    fdf.sort_values(by='creation_time').to_csv(os.path.join(
        utilities.dataset_path, f"{fname}"), columns=columns, header=columns, index=False)

    utilities.delete_extracted_files(extracted_fpath)

    print(fname, 'formatted \n')
