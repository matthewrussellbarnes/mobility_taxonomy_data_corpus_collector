import utilities
import os

import wget


def download_files(my_url, dest_folder_path):
    links = []
    alinks, base = utilities.get_download_setup(my_url)
    for alink in alinks:
        current_link = alink.get('href')
        if 'raw' in current_link and 'blob' not in current_link:
            full_alink = base.netloc + current_link
            links.append(base.scheme + "://" + full_alink)
            links = list(dict.fromkeys(links))

    utilities.wget_links(links, dest_folder_path)
