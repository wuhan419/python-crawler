# -*- coding: utf-8 -*-
__author__ = 'Sean Lei&wuhan'

from base_crawler import BaseCrawler
from pyquery import PyQuery as Pq
from dao import Dao


class VideoDetailCrawler(BaseCrawler):
    def __init__(self, seed_url):
        self._seed_url = seed_url
        self.__video_detail = {
            'id': '',
            'name': '',
            'url': '',
            'img': '',
            'maker': ''
        }
        self.__tags = []
        self.__cast = []

    def _visit_pages(self):
        """
        @override
        in this class ,only one page
        """
        html = self.get_page_content_str(self._seed_url)
        self._extract_data(html)

    def _extract_data(self, doc_str):
        doc = Pq(doc_str)
        #url
        self.__video_detail["url"] = doc('div>h3>a').attr("href")
        #image
        self.__video_detail["img"] = doc('img').filter('#video_jacket_img').attr("src")
        #name 片名
        self.__video_detail["name"] = doc('div>h3>a').text()
        #ID 识别码
        doc2 = Pq(doc('div').filter("#video_id"))
        self.__video_detail["id"] = doc2("td").filter(".text").text()
        #maker 制作商
        doc2 = Pq(doc('div').filter("#video_maker"))
        self.__video_detail["maker"] = doc2("span").filter(".maker").text()
        #tag
        doc2 = Pq(doc('div').filter("#video_genres"))
        for tag in doc2("a[rel='category tag']").text().split(" "):
            if tag is not None:
                video_tag = {
                    'video_id': self.__video_detail["id"],
                    'tag': tag
                }
                self.__tags.append(video_tag)
            else:
                continue
        # cast #演员
        doc2 = Pq(doc('div').filter("#video_cast"))
        for cast in doc2("a[rel='tag']").text().split(" "):
            if cast is not None:
                video_cast = {'video_id': self.__video_detail["id"], 'actor': cast}
                print("video_cast is ", video_cast)
                self.__cast.append(video_cast)
            else:
                continue
        self._video_dao()

    def _insert_cast(self, video_cast1):
        return "INSERT INTO video_cast (video_id,actor)" \
               " VALUES ('{}','{}' )".format(video_cast1["video_id"], video_cast1["actor"])

    def _insert_tags(self, tag1):
        return "INSERT INTO av_tag (video_id,video_tag )" \
               " VALUES ('{}','{}' )".format(tag1["video_id"], tag1["tag"])

    def _insert_video(self):
        return "INSERT INTO av_info_main (video_id,video_name,video_src,img,maker )" \
               " VALUES ('{}','{}','{}','{}','{}' )".format(self.__video_detail["id"],
                                                            self.__video_detail["name"],
                                                            self.__video_detail["url"],
                                                            self.__video_detail["img"],
                                                            self.__video_detail["maker"])

    def _video_dao(self):
        dao = Dao()
        #表中是否已有记录
        query_sql = "SELECT * FROM av_info_main WHERE video_id='{}' AND maker = '{}'".format(self.__video_detail["id"],
                                                                                             self.__video_detail[
                                                                                                 "maker"])
        if dao.execute_query(query_sql):
            print("video{} is already exists ,so next".format(self.__cast[0]["video_id"]))
            return
        #数据插入操作
        insert_sqls = []
        insert_sqls.extend(list(map(self._insert_cast, self.__cast)))
        insert_sqls.extend(list(map(self._insert_tags, self.__tags)))
        insert_sqls.append(self._insert_video())
        dao.execute_dmls(insert_sqls)


if __name__ == '__main__':
    v1 = VideoDetailCrawler("http://www.javlibrary.com/cn/?v=javlij3by4")
    v1.craw()