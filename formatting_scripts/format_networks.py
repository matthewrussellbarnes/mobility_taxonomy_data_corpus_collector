import os

import utilities

import classical_piano
import reuters_terror_news
import charnet

if not os.path.exists(utilities.dataset_path):
    os.mkdir(utilities.dataset_path)

# amazon_ratings
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'amazon_ratings.csv.zip'), specific_file='edges.csv')
utilities.format_dataset(
    fpath, columns=['# source', ' target', ' time'], fname='amazon_ratings.csv', delimiter=',')

# apostles_bible
charnet.format_dataset(os.path.join(
    utilities.dataset_path, 'acts.dat'), 'apostles_bible.csv', first_line=82)

# apollonius
charnet.format_dataset(os.path.join(
    utilities.dataset_path, 'apollonius.dat'), 'apollonius.csv', first_line=102)

# cit_us_patents
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'us_patents.csv.zip'), specific_file='edges.csv')


def remove_unspecified_gdate(col, df):
    return df.loc[df[col] != -1]


if fpath:
    nf = open(fpath.replace('edges.csv', 'nodes1.csv'), "w")
    for line in open(fpath.replace('edges.csv', 'nodes.csv'), "r"):
        if ',"' in line:
            nf.write(line[:line.index(',"')] + '\n')
        else:
            nf.write(line)
    nf.close()

    utilities.format_dataset_2file(fpath, fpath.replace('edges.csv', 'nodes1.csv'),
                                   columns=['# source', ' target', ' GYEAR'], join_columns=['# source', '# index'],
                                   fname='cit_us_patents.csv', delimiter=',', creation_time_func=remove_unspecified_gdate)

# classical_piano
classical_piano.format_dataset(os.path.join(
    utilities.dataset_path, "classical_piano.gexf"))

# CollegeMsg
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'CollegeMsg.txt.gz'))
utilities.format_headerless_dataset(
    fpath, 3, 0, 1, 2, fname='CollegeMsg.csv', delimiter=' ')

# email-Eu-core-temporal
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'email-Eu-core-temporal.txt.gz'))
utilities.format_headerless_dataset(
    fpath, 3, 0, 1, 2, fname='email-Eu-core.csv', delimiter=' ')

# eu_procurements
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'eu_procurements.zip'), specific_file='data/contracts.csv')
utilities.format_dataset(
    fpath, columns=['issuer_id_final', 'winner_id_final', 'date_dispatched'], fname='eu_procurements.csv', delimiter=',')

# facebook_wall
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'facebook_wall.csv.zip'), specific_file='edges.csv')
utilities.format_dataset(
    fpath, columns=['# source', ' target', ' time'], fname='facebook_wall.csv', delimiter=',')

# lotr
utilities.format_headerless_dataset(os.path.join(
    utilities.dataset_path, 'lotr.csv'), 3, 0, 1, 2, delimiter=',')

# luke_bible
charnet.format_dataset(os.path.join(
    utilities.dataset_path, 'luke.dat'), 'luke_bible.csv', first_line=82)

# phd_exchange

# programming_language_influence

# reuters_terror_news
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'reuters_terror_news.zip'), specific_file='daysAll.net')
reuters_terror_news.format_dataset(fpath)

# route_net
utilities.format_headerless_dataset(
    os.path.join(utilities.dataset_path, 'route_net.txt'), 3, 0, 1, 2, fname='route_net.csv', delimiter=' ')

# SCOTUS_majority
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'SCOTUS_majority.csv.zip'), specific_file='edges.csv')


def only_year_in_lexid(col, df):
    df[col] = df[col].str[:4]
    return df


if fpath:
    utilities.format_dataset_2file(fpath, fpath.replace('edges.csv', 'nodes.csv'),
                                   columns=['# source', ' target', ' lexid'], join_columns=['# source', '# index'],
                                   fname='SCOTUS_majority.csv', delimiter=',', creation_time_func=only_year_in_lexid)

# soc-redditHyperlinks-body
utilities.format_dataset(
    os.path.join(utilities.dataset_path, 'soc-redditHyperlinks-body.tsv'), columns=['SOURCE_SUBREDDIT', 'TARGET_SUBREDDIT', 'TIMESTAMP'], fname='soc-redditHyperlinks-body.csv', delimiter='\t')

# soc-redditHyperlinks-title
utilities.format_dataset(
    os.path.join(utilities.dataset_path, 'soc-redditHyperlinks-title.tsv'), columns=['SOURCE_SUBREDDIT', 'TARGET_SUBREDDIT', 'TIMESTAMP'], fname='soc-redditHyperlinks-title.csv', delimiter='\t')

# sp_hospital
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'sp_hospital.csv.zip'), specific_file='edges.csv')
utilities.format_dataset(
    fpath, columns=['# source', ' target', ' time'], fname='sp_hospital.csv', delimiter=',')

# sp_hypertext_conference
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'sp_hypertext_conference.csv.zip'), specific_file='edges.csv')
utilities.format_dataset(
    fpath, columns=['# source', ' target', ' time'], fname='sp_hypertext_conference.csv', delimiter=',')

# sp_office
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'sp_office.csv.zip'), specific_file='edges.csv')
utilities.format_dataset(
    fpath, columns=['# source', ' target', ' time'], fname='sp_office.csv', delimiter=',')

# sp_infectious
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'sp_infectious.csv.zip'), specific_file='edges.csv')
utilities.format_dataset(
    fpath, columns=['# source', ' target', ' time'], fname='sp_infectious.csv', delimiter=',')

# sp_primary_school
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'sp_primary_school.csv.zip'), specific_file='edges.csv')
utilities.format_dataset(
    fpath, columns=['# source', ' target', ' time'], fname='sp_primary_school.csv', delimiter=',')

# sx-askubuntu
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'sx-askubuntu.txt.gz'))
utilities.format_headerless_dataset(
    fpath, 3, 0, 1, 2, fname='sx-askubuntu.csv', delimiter=' ')

# sx-mathoverflow
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'sx-mathoverflow.txt.gz'))
utilities.format_headerless_dataset(
    fpath, 3, 0, 1, 2, fname='sx-mathoverflow.csv', delimiter=' ')

# sx-stackoverflow
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'sx-stackoverflow.txt.gz'))
utilities.format_headerless_dataset(
    fpath, 3, 0, 1, 2, fname='sx-stackoverflow.csv', delimiter=' ')

# sx-superuser
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'sx-superuser.txt.gz'))
utilities.format_headerless_dataset(
    fpath, 3, 0, 1, 2, fname='sx-superuser.csv', delimiter=' ')

# ucla_net
utilities.format_headerless_dataset(
    os.path.join(utilities.dataset_path, 'ucla_net.txt'), 3, 0, 1, 2, fname='ucla_net.csv', delimiter=' ')

# us_air_traffic
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'us_air_traffic.csv.zip'), specific_file='edges.csv')


def combine_year_month(col, df):
    df[col] = df[' year'].astype('str').str.cat(
        df[' month'].astype('str'), sep='-')
    return df


utilities.format_dataset(
    fpath, columns=['# source', ' target', ' time'], fname='us_air_traffic.csv', delimiter=',', creation_time_func=combine_year_month)

# wiki-talk-temporal
fpath = utilities.extract_dataset(os.path.join(
    utilities.dataset_path, 'wiki-talk-temporal.txt.gz'))
utilities.format_headerless_dataset(
    fpath, 3, 0, 1, 2, fname='wiki-talk-temporal.csv', delimiter=' ')
