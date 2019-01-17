import os
import re
import requests


class Browser:

    @staticmethod
    def get_cache_filename(url):
        # Ref: https://en.wikipedia.org/wiki/Filename at "reserved characters"
        cache_filename = 'cache/dl-' + re.sub(r'[\"\*\/\:\<\>\?\\\|]', '-', url)
        return cache_filename

    @staticmethod
    def browse_url(url):
        # If it has been downloaded before, then return the downloaded file
        cache_filename = Browser.get_cache_filename(url)
        if os.path.isfile(cache_filename):
            with open(cache_filename, 'rt') as f:
                content = f.read()
                return content
        # Otherwise download it from the web
        response = requests.get(url=url)
        content = response.content.decode(encoding='utf-8')
        with open(cache_filename, 'wt') as f:
            f.write(content)
        return content

    @staticmethod
    def download_file(url):
        # If it has been downloaded before, then return
        cache_filename = Browser.get_cache_filename(url)
        if os.path.isfile(cache_filename):
            return
        # Otherwise download it from the web
        # Ref: https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
        response = requests.get(url=url)
        content = response.content
        with open(cache_filename, 'wb') as f:
            f.write(content)
