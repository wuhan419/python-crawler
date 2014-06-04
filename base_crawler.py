# -*- coding: utf-8 -*-
__author__ = 'Sean Lei'

import urllib


class BaseCrawler(object):
    def __init__(self, seed_url=[]):
        self._doc_str = ''
        self._seed_url = seed_url

    def _generate_seed_url(self):
        """
        generate all url to visit
        """
        pass

    def _visit_pages(self):
        """
        visit one url,get page content
        """
        for single_url in self._seed_url:
            html = self.get_page_content_str(single_url)
            self._extract_data(html)

    def _extract_data(self, doc_str):
        pass

    @staticmethod
    def get_page_content_str(url):
        print(url)
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            request = urllib.request.Request(url=url, headers=headers)
            m_fp = urllib.request.urlopen(request, timeout=100)
            html_str = m_fp.read().decode('utf-8')
            m_fp.close()
        except urllib.error.URLError as err:
            logfile = open('test.log', 'a')
            logfile.write("Error: {} \n in  url : {}".format(err, url))
            logfile.close()
            print("error in {}.get_page_content_str".format(__name__))
            return None
        return html_str

    def craw(self):
        self._generate_seed_url()
        self._visit_pages()