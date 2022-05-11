from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
import wget
from urllib.request import urlopen
import os


def get_download_setup(my_url):
    html = urlopen(my_url).read()
    html_page = bs(html, features="lxml")
    base = urlparse(my_url)
    alinks = html_page.find_all('a')
    return alinks, base


def wget_links(links, dest_folder_path, file_name=None):
    for link in links:
        print(link)

        if file_name:
            dest_path = os.path.join(
                dest_folder_path, file_name)
        else:
            dest_path = os.path.join(
                dest_folder_path, link.split('/')[-1])

        if not os.path.exists(dest_path):
            try:
                wget.download(link, out=dest_path)
            except Exception as e:
                print(e)
        else:
            print("File already downloaded")

        print('\n')
