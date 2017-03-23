#*.* coding=utf-8 *.*
import os
import sys
import base64
import requests

from bs4 import BeautifulSoup



#soup = BeautifulSoup(html_doc,'html_parser')
'''
获取有多少页
'''
def get_gs_page_number():
    r = requests.get('http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml')
    soup= BeautifulSoup(r.content,'lxml')
    print soup

'''

'''
def get_goods_info():
    #print "hahah"
    r = requests.get("http://www.xinfadi.com.cn/marketanalysis/0/list/8737.shtml")
    soup = BeautifulSoup(r.content, 'lxml')

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

if __name__ == "__main__":
    get_goods_info()
    print "main function"

