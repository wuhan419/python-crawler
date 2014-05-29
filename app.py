# -*- coding: utf-8 -*-
__author__ = 'Sean Lei'

from video_list_crawler import VideoListCrawler
from video_detail_crawler import *

if __name__ == '__main__':
    crawler = VideoListCrawler()
    crawler.craw()
    ##crawlerdetal = VideoDetailCrawler()