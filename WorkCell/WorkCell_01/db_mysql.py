# -*- coding: utf-8 -*-
# @Time    : 2020/3/25_14:53
# @Author  : Garrett 
# @File    : db_mysql.py
# @Software: PyCharm

import pymysql

def getdata(db,sql):
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db=db,charset='utf8')
    cursor = db.cursor()
    sql = sql
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def insertdata(db,sql,parms):
    try:
        db = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db=db,charset='utf8')
        cursor = db.cursor()
        cursor.execute(sql % parms)
        db.commit()
        cursor.close()
        db.close()
        return 1
    except:
        return 0

if __name__ == '__main__':
    data = getdata('garrett','select * from test1;')
    print(data)

    # parms = ('bb')
    # sql = "insert into test1(name) values('%s')"
    # print(sql)
    # i = insertdata('garrett',sql,parms)
    # print(i)