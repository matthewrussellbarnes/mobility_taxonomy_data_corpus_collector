import os
import shutil
import pandas as pd

import utilities


def format_dataset(extracted_fpath):
    fname = 'classical_piano.csv'
    print(extracted_fpath, 'formatting')

    n1_list = []
    n2_list = []
    ct_list = []
    with open(extracted_fpath, 'r') as f:
        for row in f:
            if '<edge id' in row:
                prow = row.lstrip().replace('\n', '').split(' ')
                source = prow[2].split('=')[1].replace('"', '').split('-')
                n1_list.append(source[0])
                n2_list.append(prow[3].split(
                    '=')[1].replace('"', '').split('-')[0])
                ct_list.append(source[1])

    fdf = pd.DataFrame({'n1': n1_list, 'n2': n2_list,
                        'creation_time': ct_list})
    fdf.sort_values(by='creation_time').to_csv(
        os.path.join(utilities.dataset_path, f"{fname}"), index=False)

    utilities.delete_extracted_files(extracted_fpath)

    print(fname, 'fomatted')
