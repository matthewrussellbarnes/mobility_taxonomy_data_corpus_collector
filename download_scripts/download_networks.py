import os

import networks_skewed
import snap_stanford
import github
import utilities

dataset_path = os.path.join(os.path.dirname(os.getcwd()), 'datasets')
if not os.path.exists(dataset_path):
    os.mkdir(dataset_path)

# amazon_ratings
networks_skewed.download_files(
    'https://networks.skewed.de/net/amazon_ratings', dataset_path)

# apostles_bible https://ajholanda.github.io/charnet/

# apollonius https://ajholanda.github.io/charnet/

# cit_us_patents
networks_skewed.download_files(
    'https://networks.skewed.de/net/us_patents', dataset_path)

# classical_piano
utilities.wget_links(['https://osf.io/jpwtn/download'],
                     dataset_path, file_name='classical_piano.gexf')

# CollegeMsg
snap_stanford.download_files(
    'http://snap.stanford.edu/data/CollegeMsg.html', dataset_path)

# email-Eu-core-temporal
snap_stanford.download_files(
    'http://snap.stanford.edu/data/email-Eu-core-temporal.html', dataset_path, specific_file='email-Eu-core-temporal.txt')

# eu_procurements
utilities.wget_links(['https://zenodo.org/record/3537986/files/data.zip?download=1'],
                     dataset_path, file_name='eu_procurements.zip')

# facebook_wall
networks_skewed.download_files(
    'https://networks.skewed.de/net/facebook_wall', dataset_path)

# lotr https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_4_temporal_networks.ipynb

# luke_bible https://ajholanda.github.io/charnet/

# phd_exchange
github.download_files('https://github.com/taylordr/Temporal_Eigenvector_Centrality/blob/master/Temporal_Eigenvector_Centrality/PhD%20Exchange%20Network%20Data/PhD_exchange.txt',
                      dataset_path)


# programming_language_influence
utilities.wget_links(['https://royalsocietypublishing.org/action/downloadSupplement?doi=10.1098%2Frsif.2015.0249&file=rsif20150249supp1.pdf'],
                     dataset_path, file_name='programming_language_influence.pdf')

# reuters_terror_news
utilities.wget_links(['http://vlado.fmf.uni-lj.si/pub/networks/data/CRA/DaysAll.zip'],
                     dataset_path, file_name='reuters_terror_news.zip')

# route_net
github.download_files('https://github.com/richardclegg/FETA2/blob/master/data/route_net.txt',
                      dataset_path)

# SCOTUS_majority
networks_skewed.download_files(
    'https://networks.skewed.de/net/scotus_majority', dataset_path, specific_file='2007.csv', file_name='SCOTUS_majority.csv.zip')

# soc-redditHyperlinks-body & soc-redditHyperlinks-title
snap_stanford.download_files(
    'http://snap.stanford.edu/data/soc-RedditHyperlinks.html', dataset_path)

# sp_hospital
networks_skewed.download_files(
    'https://networks.skewed.de/net/sp_hospital', dataset_path)

# sp_hypertext_conference
networks_skewed.download_files(
    'https://networks.skewed.de/net/sp_hypertext', dataset_path, specific_file='contacts.csv', file_name='sp_hypertext_conference.csv.zip')

# sp_office
networks_skewed.download_files(
    'https://networks.skewed.de/net/sp_office', dataset_path)

# sp_infectious
networks_skewed.download_files(
    'https://networks.skewed.de/net/sp_infectious', dataset_path)

# sp_primary_school
networks_skewed.download_files(
    'https://networks.skewed.de/net/sp_primary_school', dataset_path)

# ax_askubuntu
snap_stanford.download_files(
    'http://snap.stanford.edu/data/sx-askubuntu.html', dataset_path, specific_file='sx-askubuntu.txt')

# sx-mathoverflow
snap_stanford.download_files(
    'http://snap.stanford.edu/data/sx-mathoverflow.html', dataset_path, specific_file='sx-mathoverflow.txt')

# sx-stackoverflow
snap_stanford.download_files(
    'http://snap.stanford.edu/data/sx-stackoverflow.html', dataset_path, specific_file='sx-stackoverflow.txt')

# sx-superuser
snap_stanford.download_files(
    'http://snap.stanford.edu/data/sx-superuser.html', dataset_path, specific_file='sx-superuser.txt')

# ucla_net
github.download_files('https://github.com/richardclegg/FETA2/blob/master/data/ucla_net.txt',
                      dataset_path)

# us_air_traffic
networks_skewed.download_files(
    'https://networks.skewed.de/net/us_air_traffic', dataset_path)

# wiki-talk-temporal
snap_stanford.download_files(
    'http://snap.stanford.edu/data/wiki-talk-temporal.html', dataset_path, specific_file='wiki-talk-temporal.txt')
