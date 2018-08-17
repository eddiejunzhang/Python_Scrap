#this code is not finished.

# PART 1, runable

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:19:33 2018

@author: tj863
"""

import datetime
import random

sDate=datetime.datetime(2018,1,3)
eDate=datetime.datetime(2018,1,2)
startFolder=1
endFolder=2
startPicture=1
endPicture=3
pre_url='http://img15.yixiu8.com:8080/picture/'
pre_root='C:/Users/tj863/tu11/'
#pre_root = '/home/pi/tu11/'

array_full=[]

iDate=sDate
while iDate > eDate:
    # i是pic目录的序号
    for i in range(startFolder,endFolder):
        for j in range(startPicture,endPicture):
            path= iDate.strftime('%y%m%d') +'/pic'+str(i)+'/'+str(j)+'.jpg'
            download_path=pre_url + path
            save_path = pre_root + path
            save_path_date = pre_root+iDate.strftime('%y%m%d') +'/'
            save_path_pic = save_path.rstrip(save_path.split('/')[-1])
            a=random.randint(0,len(array_full))
            print(iDate.strftime('%y%m%d') +' '+ str(i)+' ' +str(j))
            array_full.insert(a,[download_path,save_path,save_path_date,save_path_pic])
    iDate = iDate + datetime.timedelta(days = -1)
    
file_object = open('tu11path.txt', 'w')
for a in array_full:
    file_object.writelines(str(a[0])+' '+str(a[1])+' '+str(a[2])+' '+str(a[3]) + '\n')
file_object.close()
print("文件成功保存")

#PART 2, not runable

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:38:09 2018

@author: tj863
"""

import requests
import os
import time
import random

txtpath=r"tu11path.txt"
fp=open(txtpath)
array_full=[]
for linea in fp.readlines():
    array_full.append([str(i) for i in linea.split()])
 
fp.close()
#print(arrA)
#print(array_full[0][:])

for i in range(len(array_full)):
    print(array_full[i][0])
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
    #array_new=array_full.remove(...)
