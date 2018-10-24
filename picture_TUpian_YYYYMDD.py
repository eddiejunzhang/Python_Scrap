# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:29:41 2018
从TUPIAN网站上抓取图片. 典型URL是:
http://img15.website.com:8080/picture/140809/pic17/1.jpg
防止对方拒绝的方法：
1 伪装自己的身份，user-agent=Mozillaz/5.0
2 时间间隔拉长
@author: EddieJunZhang
"""

import requests
import os
import datetime
import time
import random

sDate=datetime.datetime(2018,6,30)
eDate=datetime.datetime(2018,6,1)
startFolder = 1
endFolder = 40
startPicture = 1
endPicture = 190
urla = 'http://img15.website.com:8080/picture/'
root = 'C:/Users/tj863/tu11/'
#root = '/home/pi/tu11/'

iDate=sDate
while iDate > eDate:
    # i是pic目录的序号
    for i in range(startFolder,endFolder):
        jcount = 0 #存放图片不存在的连续累计数
        #j是图片的文件序号
        for j in range(startPicture,endPicture):
            if jcount < 5:
                path= iDate.strftime('%y%m%d') +'/pic'+str(i)+'/'+str(j)+'.jpg'
                rootb=root+iDate.strftime('%y%m%d') +'/'
                url = urla + path
                path = root+path
                # 如果文件不存在则执行以下爬取代码
                if not os.path.isfile(path):
                    try:
                        kv={'user-agent':'Mozillaz/5.0'}
                        r = requests.get(url,headers=kv)
        #                r = requests.get(url)
                        if jcount == 0 :
                            print('wait 2-5 sec...')
                            time.sleep(random.randint(2,5) )#如果爬得过快，对方会强迫关闭链接
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
                                    print("文件成功保存 No. "+str(i)+'-'+str(j))
                                    print("文件成功保存 " + path)
                                    jcount = 0
        #                            time.sleep(random.randint(30,59) )#如果爬得过快，对方会强迫关闭链接
                            else:
                                jcount = 0
                                print('文件已经存在 No. '+str(i)+'-'+str(j)+' jcount= '+str(jcount))
                                print('文件已经存在 ' + path)
                        else:
                            jcount += 1
                            print('图片不存在 No. '+str(i)+'-'+str(j)+' jcount= '+str(jcount))
                            print('图片不存在 ' + path)
                    except FileNotFoundError as e:
                        print('爬取失败')
                        print(e)
                else:
                    print('图片已经下载过 ' + path)
            else:
                break
    
iDate = iDate + datetime.timedelta(days = -1)
