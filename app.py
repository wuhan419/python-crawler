# -*- coding: utf-8 -*-
__author__ = 'Sean Lei'

from video_list_crawler import VideoListCrawler


if __name__ == '__main__':
    crawler = VideoListCrawler()
    crawler.craw()
    print(crawler.detail_info_urls)