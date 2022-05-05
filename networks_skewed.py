from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
import wget
from urllib.request import urlopen
import os


def dl_csv(my_url, dest_path):
    links = []
    html = urlopen(my_url).read()
    html_page = bs(html, features="lxml")
    base = urlparse(my_url)
    for alink in html_page.find_all('a'):
        current_link = alink.get('href')
        if 'csv' in current_link:
            g = base.netloc + '/' + base.path + '/' + current_link
            full_alink = '/'.join(filter(None,
                                         list(dict.fromkeys(g.split('/')))))
            links.append(base.scheme + "://" + full_alink)

    for link in links:
        print(link)
        try:
            wget.download(link, out=os.path.join(
                dest_path, link.split('/')[-1]))
        except:
            print(" \n \n Unable to Download A File \n")
    print('\n')
