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
