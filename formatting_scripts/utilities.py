import os
import zipfile
import gzip
import shutil
import pandas as pd

dataset_path = os.path.join(os.path.dirname(os.getcwd()), 'datasets')


def format_dataset(extracted_fpath, delimiter=' ', columns=None, fname=None):
    print(extracted_fpath)

    if not fname:
        fname = os.path.splitext(os.path.basename(extracted_fpath))[0]

    check_ext(extracted_fpath)

    fdf = pd.read_csv(extracted_fpath, delimiter=delimiter)
    if columns:
        for column in columns:
            if not column in list(fdf.columns):
                raise Exception(f"Column '{column}' not in file")
    else:
        raise Exception(f"No columns chosen")

    if check_date(fdf[columns[2]]):
        fdf[columns[2]] = (pd.to_datetime(fdf[columns[2]]) -
                           pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')

    fdf.sort_values(by=columns[2]).to_csv(os.path.join(dataset_path, f"{fname}"), columns=columns, header=[
        'n1', 'n2', 'creation_name'], index=False)

    delete_extracted_files(extracted_fpath)

    print(fname, 'formatted')


def format_headerless_dataset(extracted_fpath, col_no, n1_no, n2_no, ct_no, delimiter=' ', fname=None):
    print(extracted_fpath)

    if not fname:
        fname = os.path.splitext(os.path.basename(extracted_fpath))[0]

    check_ext(extracted_fpath)

    columns = ['n1', 'n2', 'creation_time']

    names = [None] * col_no
    names[n1_no] = columns[0]
    names[n2_no] = columns[1]
    names[ct_no] = columns[2]

    fdf = pd.read_csv(extracted_fpath, names=names, delimiter=delimiter)

    if check_date(fdf[columns[2]]):
        fdf[columns[2]] = (pd.to_datetime(fdf[columns[2]]) -
                           pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')

    fdf.sort_values(by='creation_time').to_csv(os.path.join(
        dataset_path, f"{fname}"), columns=columns, header=columns, index=False)

    delete_extracted_files(extracted_fpath)

    print(fname, 'formatted')

#  ---------------------------------------


def extract_dataset(fpath, specific_file=None):
    print(fpath)
    [fname, _] = os.path.splitext('extr_' + os.path.basename(fpath))

    if fpath.endswith('zip'):
        with zipfile.ZipFile(fpath, 'r') as zip_ref:
            zip_ref.extractall(os.path.join(dataset_path, fname))
    elif fpath.endswith('gz'):
        with gzip.open(fpath, 'rb') as f_in:
            with open(os.path.join(dataset_path, fname), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    if not os.path.exists(os.path.join(dataset_path, 'archive')):
        os.mkdir(os.path.join(dataset_path, 'archive'))

    shutil.move(fpath, os.path.join(
        dataset_path, 'archive', os.path.basename(fpath)))

    return os.path.join(dataset_path, f"{fname}/{specific_file}" if specific_file else fname)

#  -----------------------------------


def check_ext(fpath):
    fext = os.path.splitext(os.path.basename(fpath))[1]
    if not fext in ['.csv', '.txt', '.tsv']:
        raise Exception(f"Formatting failed due to non-usable ext {fext}")


def check_date(col):
    try:
        pd.to_datetime(col)
        return True
    except:
        return False


def delete_extracted_files(extracted_fpath):
    if os.path.dirname(extracted_fpath) == dataset_path:
        print('deleted', extracted_fpath)
        os.remove(extracted_fpath)
    else:
        if os.path.dirname(os.path.dirname(extracted_fpath)) == dataset_path:
            print('deleted', os.path.dirname(extracted_fpath))
            shutil.rmtree(os.path.dirname(extracted_fpath))
        else:
            print('deleted', os.path.dirname(os.path.dirname(extracted_fpath)))
            shutil.rmtree(os.path.dirname(os.path.dirname(extracted_fpath)))
