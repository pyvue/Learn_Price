#*.* coding=utf-8 *.*
import os
import sys
import time

import mysqldb
#import MySQLdb


#todo 添加异常处理模块


def db_insert():
    try:
        print "开始操作"
        conn = mysqldb.connect(host='localhost', user='root', passwd='', db='goods_db', port=3306)
        conn.set_character_set('utf8')
        cur = conn.cursor()
        #cur.execute('select * from goods_info')
        '''
        构造信息的列表
        '''
        goods_info = ["'小白菜'", "'14.00'", "'12.13'", "'14.16'", "'普通'", "'斤'", "'2017-03-11'"]
        '''
        拼接sql字符串
        '''
        sql = """INSERT INTO `goods_db`.`goods_info` (`GoodsName`, `Minivalence`, `MiddlePrice`, `HighestPrice`, `Specification`, `Unit`, `DataTime`) VALUES ({}, {}, {}, {}, {}, {}, {});"""
        sql = sql.format(goods_info[0],goods_info[1],goods_info[2],goods_info[3],goods_info[4],goods_info[5],goods_info[6])
        print sql
        #cur.execute("INSERT INTO `goods_db`.`goods_info` (`GoodsName`, `Minivalence`, `MiddlePrice`, `HighestPrice`, `Specification`, `Unit`, `DataTime`) VALUES ('小白菜', '14.00', '12.13', '14.16', '普通', '斤', '2017-03-21');")
        cur.execute(sql)

        cur.close()
        conn.commit()
        conn.close()

    except mysqldb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    pass


if __name__ == '__main__':
    db_insert()
    print "main function"