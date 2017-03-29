#*.* coding=utf-8 *.*
import os

import base64
import time
import requests
import re
from bs4 import BeautifulSoup
import logging

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='run.log',
                filemode='w') # 设置级别
logging.warning('This is warning message')



host = 'http://www.xinfadi.com.cn'
middle_url  = '/marketanalysis/0/list/'
middle_uri = '/marketanalysis/1/list/' #蔬菜价格的中间uri
last_name = ".shtml"
#soup = BeautifulSoup(html_doc,'html_parser')

# todo 添加日志记录模块，用以排查出现的问题
# todo 添加异常处理模块，网络链接出现问题的时候，自动进行任务，无人职守才行。done
# todo 添加数据库处理模块
# todo 准备爬取蔬菜价格信息 done
# todo 解决数据编码问题  半解决，还是有很多不明白的地方，python编码是一个坑
# todo 编写查询数据库的功能代码

'''
bug 
'''
# todo 爬取完毕之后会从头开始爬，这个是一个问题，爬取完毕退出的问题
# todo 最后一页可能不满足规定的 td ，解析页面的时候需要重新写



'''
获取有多少页
'''


def get_gs_page_number():
    r = requests.get('http://www.xinfadi.com.cn/marketanalysis/1/list/1.shtml')
    soup= BeautifulSoup(r.content,'lxml')
    #print soup.find_all('a')
    #number = soup.find_all('a')[54:55] # 这个值是固定的，一段时间内是不太会改变
    number = soup.find_all(title="尾页") # 这样更精确
    #print number[0].get('href') # 获取以后的格式是： /marketanalysis/0/list/8758.shtml
    last_page_uri = number[0].get('href')
    #print last_page_uri
    '''
    使用正则表达式匹配出页码
    '''
    searchObj = re.search(r'[1-9]*\.', last_page_uri, re.M | re.I)
    number =  searchObj.group().split('.')
    number =  number[0]
    number = int(number) #转换为整型
    #print number
    #print type(number)

    return number
    #print re.search(r'[1-9]*\.',last_page_uri)
    #print (number[0].text).encode('utf-8')


'''
获取售货信息，示例如下：
绿宝调和油
5.76
5.82
5.87
普通
斤
2016-01-01
'''


def get_goods_info():
    goods_info = open('vegetables_info.txt','ab+') #货物信息保存的文件
    number = get_gs_page_number()
    print sys.getdefaultencoding()
    print "统计出页数是：".encode("gbk") + number.__str__()

    for i in range(0,number):
    #for i in range(1, 10):
        get_url= host + middle_uri + i.__str__() + last_name
        print get_url
        logging.warning(get_url)
        #time.sleep(10) # 暂停10秒钟
        '''
        考虑缩短暂停时间
        '''
        #for m in range(0,2):
        #    time.sleep(1)
        #    print '暂停中: '.encode("gbk") + (5-m).__str__()
        time.sleep(1)
        try :
            r = requests.get(get_url)
        except Exception,e :
            print e.args
            logging.warning(e.args)
        else:
            soup = BeautifulSoup(r.content, 'lxml') #解析网页
        '''
         查找所有的tag，并列出,这部分挺重要
        '''
        #for tag in soup.find_all(True):
        #    print(tag.name)

        #table_con = soup.find_all('table')[1:2]
        #print table_con
        print len(soup.find_all('td'))
        for table_d in soup.find_all('td')[16:176]:
            print table_d.text
            goods_info.write((table_d.text).encode('utf-8')) #写入到文件中
            goods_info.write('\n')

    goods_info.close() #  爬取完毕，关闭文件
    print "爬取结束。。。。".encode("gbk")
if __name__ == "__main__":
    '''
    添加异常处理
    '''
# todo 异常模块需要重新写
    try:
        get_goods_info()
    except Exception ,e:
        logging.warning(e.args)
    finally:
        get_goods_info()
    print "main function"

