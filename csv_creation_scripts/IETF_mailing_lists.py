import utilities
import os
import pandas as pd

path = os.path.join(utilities.dataset_path, "Social/IETF.csv")

ietf_df = pd.read_csv(path, header=0, sep=' ')
mailing_lists = list(set(ietf_df['Mailinglist_type']))
for ml in mailing_lists:
    ietf_df_filtered = ietf_df.query(f"Mailinglist_type == '{ml}'")

    ietf_df_filtered.to_csv(
        f'./datasets/Social/.IETF_mailing_list_{ml}.csv', index=False, sep=' ')
