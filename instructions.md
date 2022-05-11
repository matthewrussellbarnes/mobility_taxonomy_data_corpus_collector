amazon_ratings https://networks.skewed.de/net/amazon_ratings

    amazon_ratings_2010.txt
    1 -> n1
    2 -> n2
    3 -> weight
    4 -> creation_time

    (order by creation_time)

apostles_bible https://ajholanda.github.io/charnet/

    see: charnet.py

apollonius https://ajholanda.github.io/charnet/

```
	select unique tmp.n1, tmp.column1 as n2, tmp1.creation_time
	from (select n1, column1 as n2, cast(case length(cast(creation_time as varchar2(4)))
	when 3 then substr(cast(creation_time as varchar2(10)),1,2)||'0'||substr(cast(creation_time as varchar2(10)),3,1)
	else cast(creation_time as varchar2(10)) end as decimal(10,2))*100 as creation_time from tmp) tmp1 ,tmp
	where tmp1.n1 = tmp.n1 (+)
	and tmp1.n2 = tmp.column1(+)
	order by tmp1.creation_time;
```

    see: charnet.py

cit_us_patents https://networks.skewed.de/net/us_patents

    edges.csv
    source -> n1
    target -> n2

    nodes.csv
    gyear -> creation_time
    (where gyear != -1)

    Files joined by
    edges.source = nodes.index

    (order by creation_time)

classical_piano

    see: classical_piano_script.py

CollegeMsg http://snap.stanford.edu/data/CollegeMsg.html

    CollegeMsg.csv
    1 -> n1
    2 -> n2
    3 -> creation_time

email-Eu-core-temporal http://snap.stanford.edu/data/email-Eu-core-temporal.html

    email-Eu-core-temporal.csv
    1 -> n1
    2 -> n2
    3 -> creation_time

eu_procurements https://zenodo.org/record/3537986#.Xis4mC2ZNGV

    contracts.csv
    issuer_id_final -> n1
    winner_id_final -> n2
    date_dispatched -> creation_time

    (order by creation_time)

facebook_wall https://networks.skewed.de/net/facebook_wall

    facebook_wall.txt
    1 -> n1
    2 -> n2
    3 -> weight
    4 -> creation_time

lotr

    lotr.csv
    1 -> n1
    2 -> n2
    3 -> creation_time

luke_bible https://ajholanda.github.io/charnet/
see: charnet.py

phd_exchange https://github.com/taylordr/Temporal_Eigenvector_Centrality/tree/master/Temporal_Eigenvector_Centrality/PhD%20Exchange%20Network%20Data

    phd_exchange.txt
    1 -> n1
    2 -> n2
    3 -> weight
    4 -> creation_time

programming_language_influence https://royalsocietypublishing.org/action/downloadSupplement?doi=10.1098%2Frsif.2015.0249&file=rsif20150249supp1.pdf

    see: programming_language_script.py

    (order by creation_time)

reuters_terror_news http://vlado.fmf.uni-lj.si/pub/networks/data/CRA/terror.htm

    daysAll.net
    1 -> n1
    2 -> n2
    3 -> weight
    4 -> creation_time

route_net https://github.com/richardclegg/FETA2/tree/master/data

    route_net.txt
    1 -> n1
    2 -> n2
    3 -> creation_time

SCOTUS_majority https://networks.skewed.de/net/scotus_majority

    2007.csv

    edges.csv
    Source ->  n1
    Target -> n2

    nodes.csv
    First 4 characters from lexid -> creation_time

    Files joined by
    edges.source = nodes.index

    (order by creation time)

soc-redditHyperlinks-body http://snap.stanford.edu/data/soc-RedditHyperlinks.html

    soc-redditHyperlinks-body.tsv
    1 -> n1
    2 -> n2
    4 -> creation_time

    (order by creation time)

soc-redditHyperlinks-title http://snap.stanford.edu/data/soc-RedditHyperlinks.html

    soc-redditHyperlinks-title.tsv
    1 -> n1
    2 -> n2
    4 -> creation_time

    (order by creation time)

sp_hospital

    (order by creation time)

sp_hypertext_conference

    (order by creation time)

sp_office

    (order by creation time)

sp_primary_school

    (order by creation time)

ax_askubuntu

sx-mathoverflow

sx-stackoverflow

sx-superuser

ucla_net https://github.com/richardclegg/FETA2/tree/master/data

    ucla_net.txt
    1 -> n1
    2 -> n2
    3 -> creation_time

us_air_traffic https://networks.skewed.de/net/us_air_traffic

    edges.csv
    source -> n1
    target -> n2
    year-quarter-month -> creation_time

    (order by creation time)

wiki-talk-temporal

    (order by creation time)
