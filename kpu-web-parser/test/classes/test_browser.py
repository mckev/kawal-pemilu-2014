import os
import unittest

from classes.browser import Browser


class TestBrowser(unittest.TestCase):
    url = 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=8593&parent=8597'

    def test_get_cache_filename(self):
        cache_filename = Browser.get_cache_filename(TestBrowser.url)
        expected = 'cache/dl-https---pilpres2014.kpu.go.id-c1.php-cmd=select&grandparent=8593&parent=8597'
        self.assertEqual(cache_filename, expected)

    def test_download_url(self):
        # Delete cache file if exists
        cache_filename = Browser.get_cache_filename(TestBrowser.url)
        if os.path.isfile(cache_filename):
            os.remove(cache_filename)

        # Test retrieving content from direct download
        self.assertFalse(os.path.isfile(cache_filename))
        content01 = Browser.browse_url(TestBrowser.url)
        self.assertTrue(os.path.isfile(cache_filename))
        self.assertIn('SUMATERA UTARA', content01)

        # Test retrieving content from cache file
        content02 = Browser.browse_url(TestBrowser.url)
        self.assertTrue(os.path.isfile(cache_filename))
        self.assertEqual(content01, content02)

        # Delete cache file
        os.remove(cache_filename)
        self.assertFalse(os.path.isfile(cache_filename))
