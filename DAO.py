__author__ = 'wuhan'
import mysql.connector
import copy
from configparser import ConfigParser


class Dao(object):
    def __init__(self):
        config = ConfigParser()
        config.read("config.ini")
        self.__user = config.get("dbconfig", "user")
        self.__pwd = config.get("dbconfig", "pwd")
        self.__db_host = config.get("dbconfig", "db_host")
        self.__db = config.get("dbconfig", "db")

    def execute_dml(self, sql):
        """
        execute sql update and insert
        :param sql:
        :return:
        """

        cnx = mysql.connector.connect(user=self.__user, password=self.__pwd, host=self.__db_host, database=self.__db)
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

    def execute_query(self, sql):
        """
        execute sql query
        :param sql:
        :return: result_list
        """

        cnx = mysql.connector.connect(user=self.__user, password=self.__pwd, host=self.__db_host, database=self.__db)
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

if __name__ == '__main__':
    Dao = Dao()
