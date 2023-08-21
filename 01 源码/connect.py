"""
@author:兵慌码乱
@project_name:python图书管理系统
@time:2021/06/01 17:51
@remarks:数据库链接模块
"""
import pymysql


# 数据库链接
def connect():
    conn = pymysql.connect(host='localhost', user='root', password='root', database='library')
    cursor = conn.cursor()
    return cursor, conn
