# -*- coding: utf-8 -*-
import copy

__author__ = 'wuhan'
#-------------------------import part-----------------
import re
import urllib.request

import mysql.connector
from bs4 import BeautifulSoup


#----------------------------------begin-------
defaultCharacterSet = "utf8"

#TODO 干掉这个文件吧
def find_av(a, host, headers):
    # global cursor
    video_detail = {
        'id': '',
        'name': '',
        'link': "",
        'img': '',
        'maker': ''
    }
    for a1 in a:
        print(a1, 'begin ')
        tags = []
        cast = []
        #找到片子的页面 用beautiful soup提取源码
        # print(a1.string + " begin")
        target_url = host + a1["href"]
        req = urllib.request.Request(url=target_url, headers=headers)
        fp = urllib.request.urlopen(req)
        mybytes = fp.read()
        fp.close()
        mystr = mybytes.decode(defaultCharacterSet)
        soup = BeautifulSoup(mystr, from_encoding=defaultCharacterSet)
        video_detail["link"] = target_url
        #图片
        tag = soup("img", id='video_jacket_img')
        # print(tag[0]["src"])  ##tag is a list ,even it only have a single row
        video_detail["img"] = tag[0]["src"]
        #片名
        tag = soup("a", {'rel': "bookmark", "href": re.compile("http://+")})
        # print(tag)
        video_detail["name"] = tag[0].string
        #识别码
        tag = soup.select("div#video_id  td[class~=text]")
        video_detail["id"] = tag[0].string
        #maker
        tag = soup.select("div#video_maker  td[class~=text] a[rel~=tag]")
        video_detail["maker"] = tag[0].string.replace(" ", "")
        ##tag
        for tag in soup("a", rel="category tag"):
            ##f.write()TypeError: must be str, not None
            #这里不是判断字符串空，而是判断none type
            if tag.string is None:
                continue
            else:
                video_tag = {
                    'video_id': '',
                    'tag': ''
                }
            video_tag['video_id'] = video_detail["id"]
            video_tag['tag'] = tag.string
            tags.append(video_tag)

        for actor in soup("a", {"href": re.compile("vl_star\.php\?s=+")}):
            #f.write()TypeError: must be str, not None
            #这里不是判断字符串空，而是判断none type
            if actor.string is None:
                continue
            else:
                #演员
                video_cast = {'video_id': video_detail["id"], 'actor': actor.string, 'url': actor["href"]}
                print("video_cast is ", video_cast)
                cast.append(video_cast)

        #表中是否已有记录

        query_sql = "select * from av_info_main where video_id='{}' and maker = '{}'".format(video_detail["id"],
                                                                                             video_detail["maker"])
        if execute_query(query_sql):
            print("video{} is already exists ,so next".format(cast[0]["video_id"]))
            continue

        #数据插入操作
        for video_cast1 in cast:
            #myset = video_cast1.split()
            # print(video_cast1["id"], video_cast1["name"], video_cast1["link"], video_cast1["img"])
            insert_sql = "INSERT INTO video_cast (video_id,actor,url)" \
                         " VALUES ('{}','{}','{}' )".format(video_cast1["video_id"], video_cast1["actor"],
                                                            video_cast1["url"])
            execute_update(insert_sql)
        for tag1 in tags:
            #myset = video_cast1.split()
            # print(video_cast1["id"], video_cast1["name"], video_cast1["link"], video_cast1["img"])
            insert_sql = "INSERT INTO av_tag (video_id,video_tag )" \
                         " VALUES ('{}','{}' )".format(tag1["video_id"], tag1["tag"])
            execute_update(insert_sql)
        insert_sql = "INSERT INTO av_info_main (video_id,video_name,video_src,img,maker )" \
                     " VALUES ('{}','{}','{}','{}','{}' )".format(video_detail["id"], video_detail["name"],
                                                                  video_detail["link"], video_detail["img"],
                                                                  video_detail["maker"])
        execute_update(insert_sql)


def execute_update(sql):
    """
    execute sql update and insert
    :param sql:
    :return:
    """
    user = 'avoper'
    pwd = '******'
    db_host = '127.0.0.1'
    db = 'avdb'
    cnx = mysql.connector.connect(user=user, password=pwd, host=db_host, database=db)
    print(sql)
    cursor = cnx.cursor()
    try:
        cursor.execute(sql)
    except mysql.connector.Error as sql_err:
        print("Error: {}".format(sql_err.msg))
        log_sql = open('test.log', 'a')
        log_sql.write("Error: {} \n in the insert/update sql :{}".format(sql_err.msg, sql))
        log_sql.close()
    cnx.commit()
    cursor.close()
    cnx.close


def execute_query(sql):
    """
    execute sql query
    :param sql:
    :return: result_list
    """
    user = 'avoper'
    pwd = '******'
    db_host = '127.0.0.1'
    db = 'avdb'
    cnx = mysql.connector.connect(user=user, password=pwd, host=db_host, database=db)
    print(sql)
    cursor = cnx.cursor()
    try:
        cursor.execute(sql)
        result_rows = copy.deepcopy(cursor.fetchone())
        if result_rows:
            print(result_rows)
            cursor.close()
            cnx.close
            return result_rows
        if result_rows is None:
            print("reuslt is null")
            cursor.close()
            cnx.close
            return None
    except mysql.connector.Error as sql_err:
        print("Error: {}".format(sql_err.msg))
        log_sql = open('test.log', 'a')
        log_sql.write("Error: {} \n in the insert/update sql :{}".format(sql_err.msg, sql))
        log_sql.close()

        #cursor.close()


if __name__ == "__main__":
    host = "http://www.javlibrary.com/cn/"
    url = "vl_update.php?list&mode=&page="
    # page = "1"
    for page in range(1, 202):
        print("begin the page ", page)
        chaper_url = host + url + page.__str__()
        #给request 报文加headers
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        #获取到报文,转码
        try:
            m_req = urllib.request.Request(url=chaper_url, headers=headers)
            m_fp = urllib.request.urlopen(m_req, timeout=100)
            m_mybytes = m_fp.read()
            #别忘了关
            m_fp.close()
            # note that Python3 does not read the html code as string
            # but as html code bytearray, convert to string with
            m_mystr = m_mybytes.decode(defaultCharacterSet)
            soup_all = BeautifulSoup(m_mystr, from_encoding=defaultCharacterSet)
            #正则匹配./? 开头的href
            a = soup_all.find_all("a", {"href": re.compile("\./\?+")})
            # path_w = 'D:\workspace\python\AVspider\web.txt'
            #文件输出的时候必须要制定编码 否则会报错,f = open(path_w,"w",encoding='utf-8')
            ##后来看网上说用wb做参数可以写入空，试了试，不行。。。
            find_av(a, host, headers)
            print("page :{} finished".format(page))
        except urllib.error.URLError as err:
            logfile = open('test.log', 'a')
            logfile.write("Error: {} \n in page :{} url : {}".format(err, page, chaper_url))
            logfile.close()
            print("error in __main__")
        print('ok')



