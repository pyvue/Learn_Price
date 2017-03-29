#*.* coding=utf-8 *.*
import os
import sys
import time

import mysqldb
#import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#todo 添加异常处理模块

'''
数据库插入数据
'''
def db_insert(info_list):
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
        goods_info = []
        goods_info = info_list
        print goods_info
        '''
        拼接sql字符串
        '''
        sql = """INSERT INTO `goods_db`.`goods_info` (`GoodsName`, `Minivalence`, `MiddlePrice`, `HighestPrice`, `Specification`, `Unit`, `DataTime`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');"""
        sql = sql.format(goods_info[0],goods_info[1],goods_info[2],goods_info[3],goods_info[4],goods_info[5],goods_info[6])
        print sql
        #cur.execute("INSERT INTO `goods_db`.`goods_info` (`GoodsName`, `Minivalence`, `MiddlePrice`, `HighestPrice`, `Specification`, `Unit`, `DataTime`) VALUES ('小白菜', '14.00', '12.13', '14.16', '普通', '斤', '2017-03-21');")
        cur.execute(sql)

        cur.close()
        conn.commit()
        conn.close()

    except mysqldb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


'''
格式化数据
'''

def data_format():
        f = open("goods_info.txt","r")
        #line_number = len(f.readlines())  # 文件行数
        #print line_number
        i = 0
        buff = f.readlines()
        info_list = []
        for line in buff:
            info_list.append(line.strip('\n'))
            if len(info_list) == 8 :
               #print "信息长度为8了\n"
               info_list.pop() # 删除最后一个空格
               print info_list[0].decode("utf-8") # 解决编码问题
               db_insert(info_list)    # 插入数据库
               time.sleep(0.1)
               info_list = [] # 清空列表
            i += 1
        print i
        f.close()


        #print os.path.getsize("goods_info.txt") # 文件大小
        #line_number = len(f.readlines())                # 文件行数






if __name__ == '__main__':
    #db_insert()
    data_format()
    print "main function"