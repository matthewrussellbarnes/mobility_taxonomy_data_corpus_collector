import os
import zipfile
import gzip
import shutil
import pandas as pd

dataset_path = os.path.join(os.path.dirname(os.getcwd()), 'datasets')


def format_dataset(extracted_fpath, delimiter=' ', columns=None, fname=None, creation_time_func=None):
    print(extracted_fpath, 'formatting')

    if not fname:
        fname = os.path.splitext(os.path.basename(extracted_fpath))[0]

    check_ext(extracted_fpath)

    fdf = pd.read_csv(extracted_fpath, delimiter=delimiter)

    if creation_time_func:
        fdf = creation_time_func(columns[2], fdf)

    check_columns_in_df(fdf, columns)

    fdf[columns[2]] = convert_df_date_col_to_unix(fdf, columns[2])

    fdf.sort_values(by=columns[2]).to_csv(os.path.join(dataset_path, f"{fname}"), columns=columns, header=[
        'n1', 'n2', 'creation_time'], index=False)

    delete_extracted_files(extracted_fpath)

    print(fname, 'formatted')


def format_dataset_2file(fpath1, fpath2, fname, delimiter=' ', columns=None, join_columns=None, creation_time_func=None):
    print(fpath1, fpath2, 'formatting')

    check_ext(fpath1)
    check_ext(fpath2)

    f1df = pd.read_csv(fpath1, delimiter=delimiter)

    f2df = pd.read_csv(fpath2, delimiter=delimiter, quotechar='"')

    jdf = f1df.join(f2df.set_index(join_columns[1]), on=join_columns[0])

    if creation_time_func:
        jdf = creation_time_func(columns[2], jdf)

    check_columns_in_df(jdf, columns)

    jdf[columns[2]] = convert_df_date_col_to_unix(jdf, columns[2])

    jdf.sort_values(by=columns[2]).to_csv(os.path.join(dataset_path, f"{fname}"), columns=columns, header=[
        'n1', 'n2', 'creation_time'], index=False)

    delete_extracted_files(fpath1)

    print(fname, 'formatted')


def format_headerless_dataset(extracted_fpath, col_no, n1_no, n2_no, ct_no, delimiter=' ', fname=None):
    print(extracted_fpath, 'formatting')

    if not fname:
        fname = os.path.splitext(os.path.basename(extracted_fpath))[0]

    check_ext(extracted_fpath)

    columns = ['n1', 'n2', 'creation_time']

    names = [None] * col_no
    names[n1_no] = columns[0]
    names[n2_no] = columns[1]
    names[ct_no] = columns[2]

    fdf = pd.read_csv(extracted_fpath, names=names, delimiter=delimiter)

    fdf[columns[2]] = convert_df_date_col_to_unix(fdf, columns[2])

    fdf.sort_values(by='creation_time').to_csv(os.path.join(
        dataset_path, f"{fname}"), columns=columns, header=columns, index=False)

    delete_extracted_files(extracted_fpath)

    print(fname, 'formatted')

#  ---------------------------------------


def extract_dataset(fpath, specific_file=None):
    print(fpath, 'extracting')
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


def check_columns_in_df(fdf, columns):
    if columns:
        for column in columns:
            if not column in list(fdf.columns):
                raise Exception(f"Column '{column}' not in file")
    else:
        raise Exception(f"No columns chosen")

# -------------------------------------------


def convert_df_date_col_to_unix(df, col):
    if '-' in str(df[col][0]):
        return (pd.to_datetime(df[col]) -
                pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
    else:
        return df[col]

# -------------------------------------------


def delete_extracted_files(extracted_fpath):
    if os.path.dirname(extracted_fpath) == dataset_path:
        if os.path.basename(extracted_fpath).startswith('extr'):
            print(extracted_fpath, 'deleted')
            os.remove(extracted_fpath)
        else:
            print(extracted_fpath, 'moved')
            shutil.move(extracted_fpath, os.path.join(
                dataset_path, 'archive', os.path.basename(extracted_fpath)))
    else:
        if os.path.dirname(os.path.dirname(extracted_fpath)) == dataset_path:
            print(os.path.dirname(extracted_fpath), 'deleted')
            shutil.rmtree(os.path.dirname(extracted_fpath))
        else:
            print(os.path.dirname(os.path.dirname(extracted_fpath)), 'deleted')
            shutil.rmtree(os.path.dirname(os.path.dirname(extracted_fpath)))
