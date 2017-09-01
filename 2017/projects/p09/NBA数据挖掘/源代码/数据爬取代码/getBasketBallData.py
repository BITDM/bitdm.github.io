# -*- coding: utf-8 -*-

__author__ = 'LYW'
import requests
import urllib
import time
import re
import sys
import os
import os.path
import json
import random
import codecs
import MySQLdb
import csv

reload(sys)
sys.setdefaultencoding('utf-8')  # 将当前的字符处理模式修改为utf-8编码模式

csvfile = file('C:\\Users\\vv\\Desktop\\Basketball\\csv_test.csv', 'wb')
writer = csv.writer(csvfile)
csvfile.write(codecs.BOM_UTF8)
def getTime():
    time_format = '%Y-%m-%d %X'
    return time.strftime(time_format, time.localtime(time.time()))


def crawlURL(url):
    print 'Crawl'
    print 'crawl; ' + url
    # time.sleep(1)
    # time.sleep(random.randint(1,5))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    req_header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "en;q=0.8",
        "Host": "https://scholar.google.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
    }
    url = url.replace(' ', '%20')
    # proxy = {"http": "http://127.0.0.1:8087", "https": "https://127.0.0.1:8087"}  # 翻墙
    # response = requests.get('https://en.wikipedia.org/wiki/Natural_language_processing', proxies=proxy,verify=False)
    # content = response.text
    '''
    req = urllib2.Request(url, headers=headers)
    try:
        print 'go'
        content = urllib2.urlopen(req).read()
        return content
    except:
        print 'failed'
        return ''
    '''
    try:

        reload(sys)
        sys.setdefaultencoding('utf-8')  # 将当前的字符处理模式修改为utf-8编码模式
        proxy = {"http": "http://127.0.0.1:8087", "https": "https://127.0.0.1:8087"}  # 翻墙

        # print url
        response = requests.get(url)#, proxies=proxy,verify=False)
        #print response.content
        #content = response.text
        # getInfo(content)
        print 'crawlUrl'
        # self.saveUrl(url, content, 'HTML_Data')
        return response.content
    except:
        print 'get error'
        return ''

def download(url, path):
    print 'download: ' + url
    path = path.replace(r'+', '')
    #print 'path: ' + path
    if (os.path.exists(path)):
        print 'a!'
        content1 = open(path, 'r').read()
    else:
        try:
            print 'b!'
            tim = getTime()
            print 'try ' + tim
            content1 = crawlURL(url)
            if content1 == '':
                return ''
            print '@@@@'
            info2 = open(path, 'w+')
            print '!!!!'
            info2.write(content1)
            print len(content1)
            #if(len(content1) > 2000):
            time.sleep(random.randint(2, 5))
            print 'OK!'
            # print content
        except:
            print "oops! url " + url
            print 'error path ' + path
            content1 = 0
    return content1




itm1 = re.compile('<thead>.+?</thead>', re.S | re.M)
itm2 = re.compile('<tbody>.+?</tbody>', re.S | re.M)
itm3 = re.compile('<tr>.+?</tr>', re.S | re.M)
l = re.compile('<th class=.+?</th>', re.S)
r = re.compile('<td class=.+?</td>', re.S)
dr = re.compile('<.+?>', re.S)

def getTitle(content):
    cont = re.findall(itm1, content)
    titles = re.findall(l, cont[0])
    Title = ''
    A = []
    for one in titles:
        itm = re.sub(dr, '', one)
        Title = Title + itm + ','
        A.append(itm.decode('utf8'))
    print A
    writer.writerow(A)
    with open('C:\\Users\\vv\\Desktop\\Basketball\\data.txt', 'w+') as f:
        f.write(Title + '\n')




def getData(content):
    reload(sys)
    sys.setdefaultencoding('utf-8')  # 将当前的字符处理模式修改为utf-8编码模式
    cont = re.findall(itm2, content)
    cont = re.findall(itm3, cont[0])
    #print cont

    for people in cont:
        itms = re.findall(r, people)
        #print itms
        man = ''
        B = []
        for one in itms:
            itm = re.sub(dr, '', one)
            print itm
            man = man + itm + ','
            B.append(itm)
        print man
        writer.writerow(B)
        with open('C:\\Users\\vv\\Desktop\\Basketball\\data.txt', 'a+') as f:
            f.write(man + '\n')
        #Man.append(man)



#0-27
url1 = "http://www.stat-nba.com/query.php?page="
url2 = "&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts" \
      "&PageNum=150#label_show_result"
root = 'C:/Users/vv/Desktop/Basketball'
for i in range(0, 28):
    print i
    content = download(url1 + str(i) + url2, root + '/' + str(i) + '.html')

    if i == 0:
        getTitle(content)
    getData(content)
    #print content

csvfile.close()