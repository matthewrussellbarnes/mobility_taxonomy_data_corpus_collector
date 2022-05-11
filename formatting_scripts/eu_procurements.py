import os
import shutil
import pandas as pd

import utilities


def format_dataset(extracted_fpath):
    delimiter = ','
    columns = ['issuer_id_final', 'winner_id_final', 'date_dispatched']
    fname = 'eu_procurements.csv'
    print(extracted_fpath)

    utilities.check_ext(extracted_fpath)

    fdf = pd.read_csv(extracted_fpath, delimiter=delimiter)
    fdf[columns[2]] = (pd.to_datetime(fdf[columns[2]]) -
                       pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
    fdf.sort_values(by=columns[2]).to_csv(os.path.join(utilities.dataset_path, f"{fname}"), columns=columns, header=[
        'n1', 'n2', 'creation_name'], index=False)

    print('deleted', os.path.dirname(os.path.dirname(extracted_fpath)))
    shutil.rmtree(os.path.dirname(os.path.dirname(extracted_fpath)))

    print(fname, 'fomatted')
