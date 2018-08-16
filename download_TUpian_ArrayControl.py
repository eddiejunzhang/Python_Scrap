# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 22:24:42 2018
把所有要下载的文件路径穷举出来，以乱序方式写入一个数组
按数组下载
因为怀疑按顺序下载，会导致对方封锁
数组：源文件路径，保存在磁盘上的路径，磁盘上的日期路径，磁盘上的图片路径
后两个用来判断路径是否存在，是否需要生成
@author: tj863
"""

import requests
import os
import datetime
import random
import time

sDate=datetime.datetime(2018,1,15)
eDate=datetime.datetime(2018,1,1)
startFolder=1
endFolder=10
startPicture=1
endPicture=10
pre_url='http://img15.pictures.com:8080/picture/'
pre_root='C:/Users/user/tu_p1c/'
#pre_root = '/home/pi/tu_pic/'

array_full=[]

iDate=sDate
while iDate > eDate:
    # i是pic目录的序号
    for i in range(startFolder, endFolder):
        for j in range(startPicture, endPicture):
            path = iDate.strftime('%y%m%d') + '/pic' + str(i) + '/' + str(j)+'.jpg'
            download_path = pre_url + path
            save_path = pre_root + path
            save_path_date = pre_root+iDate.strftime('%y%m%d') + '/'
            save_path_pic = save_path.rstrip(save_path.split('/')[-1])
            a=random.randint(0,len(array_full))
            print(iDate.strftime('%y%m%d') + ' ' + str(i) + ' ' +str(j))
            array_full.insert(a,[download_path, save_path, save_path_date, save_path_pic])
    iDate = iDate + datetime.timedelta(days = -1)
    
for i in range(len(array_full)):
#    print(array_full[i][0])
    try:
        kv={'user-agent':'Mozillaz/5.0'}
        r = requests.get(array_full[i][0],headers=kv)
#                r = requests.get(url)
        print('wait 2-6 sec...')
        time.sleep(random.randint(2,6) )#如果爬得过快，对方会强迫关闭链接
        if r.ok:
            if not os.path.exists(array_full[i][2]):
                os.mkdir(array_full[i][2])
            if not os.path.exists(array_full[i][3]):
                os.mkdir(array_full[i][3])
            if not os.path.exists(array_full[i][1]):
                with open(array_full[i][1],'wb') as f:
                    f.write(r.content)
                    f.close
                    print("文件成功保存 "+array_full[i][1])
            else:
                print('文件已经存在 '+array_full[i][1])
        else:
            print('图片不存在 '+array_full[i][0])
    except FileNotFoundError as e:
        print('爬取失败')
        print(e)
