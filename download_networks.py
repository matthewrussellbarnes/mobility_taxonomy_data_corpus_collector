import os

import networks_skewed
import snap_stanford

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

# CollegeMsg
snap_stanford.dl_csv(
    'http://snap.stanford.edu/data/CollegeMsg.html', dataset_path)

# email-Eu-core-temporal
snap_stanford.dl_csv(
    'http://snap.stanford.edu/data/email-Eu-core-temporal.html', dataset_path)

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

# soc-redditHyperlinks-body
# soc-redditHyperlinks-title
snap_stanford.dl_csv(
    'http://snap.stanford.edu/data/soc-RedditHyperlinks.html', dataset_path)

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
snap_stanford.dl_csv(
    'http://snap.stanford.edu/data/soc-RedditHyperlinks.html', dataset_path)

# sx-mathoverflow
snap_stanford.dl_csv(
    'http://snap.stanford.edu/data/sx-mathoverflow.html', dataset_path)

# sx-stackoverflow
snap_stanford.dl_csv(
    'http://snap.stanford.edu/data/sx-stackoverflow.html', dataset_path)

# sx-superuser
snap_stanford.dl_csv(
    'http://snap.stanford.edu/data/sx-superuser.html', dataset_path)

# ucla_net https://github.com/richardclegg/FETA2/tree/master/data

# us_air_traffic
networks_skewed.dl_csv(
    'https://networks.skewed.de/net/us_air_traffic', dataset_path)

# wiki-talk-temporal
snap_stanford.dl_csv(
    'http://snap.stanford.edu/data/wiki-talk-temporal.html', dataset_path)
