import utilities


def download_files(my_url, dest_folder_path):
    links = []
    alinks, base = utilities.get_download_setup(my_url)

    for alink in alinks:
        current_link = alink.get('href')
        if 'download' in current_link:
            g = base.netloc + '/' + base.path + '/' + current_link
            full_alink = '/'.join(filter(None,
                                         list(dict.fromkeys(g.split('/')))))
            links.append(base.scheme + "://" + full_alink)

    utilities.wget_links(links, dest_folder_path)
