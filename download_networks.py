import os

import networks_skewed

dataset_path = os.path.join(os.getcwd(), 'datasets')
if not os.path.exists(dataset_path):
    os.mkdir(dataset_path)

# amazon_ratings
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/amazon_ratings', dataset_path)

# apostles_bible https://ajholanda.github.io/charnet/

# apollonius https://ajholanda.github.io/charnet/

# cit_us_patents
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/us_patents', dataset_path)

# classical_piano https://osf.io/jvzxg/

# CollegeMsg http://snap.stanford.edu/data/CollegeMsg.html

# email-Eu-core-temporal http://snap.stanford.edu/data/email-Eu-core-temporal.html

# eu_procurements https://zenodo.org/record/3537986#.Xis4mC2ZNGV

# facebook_wall
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/facebook_wall', dataset_path)

# lotr https://github.com/IngoScholtes/kdd2018-tutorial/blob/master/code/1_4_temporal_networks.ipynb

# luke_bible https://ajholanda.github.io/charnet/

# phd_exchange https://github.com/taylordr/Temporal_Eigenvector_Centrality/tree/master/Temporal_Eigenvector_Centrality/PhD%20Exchange%20Network%20Data

# programming_language_influence https://royalsocietypublishing.org/action/downloadSupplement?doi=10.1098%2Frsif.2015.0249&file=rsif20150249supp1.pdf

# reuters_terror_news http://vlado.fmf.uni-lj.si/pub/networks/data/CRA/terror.htm

# route_net https://github.com/richardclegg/FETA2/tree/master/data

# SCOTUS_majority
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/scotus_majority', dataset_path)

# soc-redditHyperlinks-body http://snap.stanford.edu/data/soc-RedditHyperlinks.html

# soc-redditHyperlinks-title http://snap.stanford.edu/data/soc-RedditHyperlinks.html

# sp_hospital
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/sp_hospital', dataset_path)

# sp_hypertext_conference
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/sp_hypertext', dataset_path)

# sp_office
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/sp_office', dataset_path)

# sp_infectious
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/sp_infectious', dataset_path)

# sp_primary_school
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/sp_primary_school', dataset_path)

# ax_askubuntu http://snap.stanford.edu/data/sx-askubuntu.html

# sx-mathoverflow http://snap.stanford.edu/data/sx-mathoverflow.html

# sx-stackoverflow http://snap.stanford.edu/data/sx-stackoverflow.html

# sx-superuser http://snap.stanford.edu/data/sx-superuser.html

# ucla_net https://github.com/richardclegg/FETA2/tree/master/data

# us_air_traffic
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/us_air_traffic', dataset_path)

# wiki-talk-temporal