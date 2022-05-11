import pandas as pd


filename = "/Users/mattbarnes/Documents/Writing/DMSN Project Topic/datasets/1911_rachmaninov_op33-8.gexf"


df = pd.DataFrame(columns=['n1', 'n2', 'creation_time'])
with open(filename, 'r') as f:
    for row in f:
        if '<edge id' in row:
            prow = row.lstrip().replace('\n', '').split(' ')
            source = prow[2].split('=')[1].replace('"', '')
            n1 = source
            n2 = prow[3].split('=')[1].replace('"', '')
            # print(n1, n2, creation_time)

            df.loc[len(df.index)] = [
                n1, n2, 1073]

df.to_csv(f"{filename[:-5]}.tsv", index=False, sep=' ')
