# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:29:41 2018
从TU11网站上抓取图片
2018-6-30以前的
@author: EddieJunZhang
"""

import requests
import os
import datetime
import time

sDate=datetime.datetime(2018,6,30)
eDate=datetime.datetime(2018,6,1)
urla='http://img15.yixiu8.com:8080/picture/'
root='C:/Users/tj863/tu11/'

iDate=sDate
while iDate > eDate:
    for i in range(40):
        for j in range(90):
            path= iDate.strftime('%y%m%d') +'/pic'+str(i)+'/'+str(j)+'.jpg'
            rootb=root+iDate.strftime('%y%m%d') +'/'
            url = urla + path
            path = root+path
            try:
                r = requests.get(url)
                if r.ok:
                    roota = path.rstrip(path.split('/')[-1])
                    if not os.path.exists(rootb):
                        os.mkdir(rootb)
                    if not os.path.exists(roota):
                        os.mkdir(roota)
                    if not os.path.exists(path):
                        with open(path,'wb') as f:
                            f.write(r.content)
                            f.close
                            print("文件成功保存")
                            time.sleep(30)#如果爬得过快，对方会强迫关闭链接
                    else:
                        print('文件已经存在')
                else:
                    print('图片不存在')
            except FileNotFoundError as e:
                print('爬取失败')
                print(e)
    i+=1
    j+=1
    iDate = iDate + datetime.timedelta(days = -1)
