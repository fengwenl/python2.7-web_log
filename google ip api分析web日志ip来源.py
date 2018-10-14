#!/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = 'gaogd'

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as mysql
import datetime
import sys, os, urllib2, json

db = mysql.connect(user="root",passwd="root",db="intest",host="127.0.0.1") #数据库连接信息
db.autocommit(True)
cur = db.cursor()
cur.execute('set names utf8')
addtime = datetime.datetime.now()

ips = {}        #ip作为字典的key，访问次数做value
iplist = []     #遍历日志中的ip，相同的ip也会记录到列表，插入数据库
fh = open("20181006-2018-10-13.log", "r").readlines()                                                               #我的是把日志和代码在一个目录下面
for line in fh:
    ip = line.split(" ")[0]
    print ip
    if 6 < len(ip) <=15:
        ips[ip] = ips.get(ip, 0) + 1

        alist = iplist.append(ip)
for key,value in ips.items():
    listinfo = str(ips)
    sql = 'insert into ipinfo(ipaddress,countip) value ("%s","%s")' % (key,value)
    cur.execute(sql)

def get_ip_area(ip):
    try:
        apiurl = "http://ip-api.com/json/%s?lang=zh-CN" %ip#google ip api
        content = urllib2.urlopen(apiurl).read()
        data = json.loads(content) #数据转化
        if data['country']: # success
            country=(data['country'])
            area = (data['regionName'])
            region = (data['region'])
            city = (data['city'])
            ip = (data['query'])
            print(data['country']),(data['status']),(data['region']),(data['city']),(data['query'])
            #数据库写入
            sql = 'insert into whereip (country,area,region,city,ip,time) value ("%s","%s","%s","%s","%s","%s")' % (country.encode("utf-8"),area.encode("utf-8"),region.encode("utf-8"),city.encode("utf-8"),ip.encode("utf-8"),addtime)
            cur.execute(sql)
            print 'sql:',sql
        else:
            print data
    except Exception as ex:
        print ex

if __name__ == '__main__':
    for ip in iplist:
        get_ip_area(ip)
