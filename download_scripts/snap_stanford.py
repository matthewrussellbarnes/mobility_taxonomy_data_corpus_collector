import utilities


def download_files(my_url, dest_folder_path, file_name=None, specific_file=None):
    links = []
    alinks, base = utilities.get_download_setup(my_url)

    for alink in alinks:
        current_link = alink.get('href')
        if 'txt' in current_link or 'tsv' in current_link:
            if (specific_file in current_link if specific_file else True):
                g = base.netloc + '/' + \
                    base.path.split('/')[1] + '/' + current_link
                full_alink = '/'.join(filter(None,
                                             list(dict.fromkeys(g.split('/')))))
                links.append(base.scheme + "://" + full_alink)

    utilities.wget_links(links, dest_folder_path, file_name=file_name)
