import os
import pandas as pd

import utilities


def format_dataset(extracted_fpath, fname, first_line=0):
    if not extracted_fpath:
        return

    print(extracted_fpath, 'formatting')

    n1_list = []
    n2_list = []
    ct_list = []

    try:
        with open(extracted_fpath, 'r') as f:
            i = 0
            for row in f:
                i += 1
                if i >= first_line:
                    if row.startswith('* End'):
                        break

                    split_row = row.replace('\n', '').split(':')
                    creation_time = split_row[0]
                    if 'apollonius' in extracted_fpath:
                        creation_time = creation_time.replace('.', '0') if len(
                            creation_time) == 3 else creation_time.replace('.', '')
                    split_edges = split_row[1].split(';')
                    for edge in split_edges:
                        split_edge = edge.split(',')
                        if len(split_edge) == 2:
                            n1_list.append(split_edge[0])
                            n2_list.append(split_edge[1])
                            ct_list.append(creation_time)
                        else:
                            for n1 in split_edge:
                                for n2 in split_edge:
                                    if n1 != n2:
                                        n1_list.append(n1)
                                        n2_list.append(n2)
                                        ct_list.append(creation_time)

    except Exception as e:
        print(e, '\n')
        return

    fdf = pd.DataFrame({'n1': n1_list, 'n2': n2_list,
                        'creation_time': ct_list})

    fdf['creation_time'] = pd.to_numeric(fdf['creation_time'])
    fdf.sort_values(by='creation_time').to_csv(
        os.path.join(utilities.dataset_path, f"{fname}"), index=False)

    utilities.delete_extracted_files(extracted_fpath)

    print(fname, 'formatted \n')
