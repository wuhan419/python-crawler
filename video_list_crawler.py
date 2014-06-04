# -*- coding: utf-8 -*-
__author__ = 'Sean Lei'

from pyquery import PyQuery as Pq

from base_crawler import BaseCrawler
from video_detail_crawler import VideoDetailCrawler


class VideoListCrawler(BaseCrawler):
    def __init__(self):
        #TODO 用参数化和多线程来执行抓取
        super().__init__()
        self.detail_info_urls = []
        self._info_uri = '/cn/vl_update.php?list&mode=&page='
        self._detail_uri = '/cn/?v='
        self._domain = 'http://www.javlibrary.com'

    def _generate_seed_url(self):
        """
        generate all url to visit
        """
        ##from page 1 to anypage which < 200
        for page_no in range(1, 2):
            self._seed_url.append(self._domain + self._info_uri + page_no.__str__())

    def _extract_data(self, doc_str):
        doc = Pq(doc_str)
        video_list = doc('.videotextlist .title .video')
        for video in video_list:
            video_id = Pq(video).attr('id')
            video_id = video_id[4:]
            detail_url = self._domain + self._detail_uri + video_id
            self.detail_info_urls.append(detail_url)
            crawler = VideoDetailCrawler(detail_url)
            crawler.craw()
