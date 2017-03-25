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
        
    except mysqldb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    pass


if __name__ == '__main__':
    db_insert()
    print "main function"