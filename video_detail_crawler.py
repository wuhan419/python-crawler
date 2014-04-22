# -*- coding: utf-8 -*-
__author__ = 'Sean Lei'

from base_crawler import BaseCrawler
from pyquery import PyQuery as Pq


class VideoDetailCrawler(BaseCrawler):
    def _extract_data(self, doc_str):
        doc = Pq(doc_str)
        print(doc)
        pass