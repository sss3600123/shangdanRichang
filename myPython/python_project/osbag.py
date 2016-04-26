import os.path
import time
import datetime
import glob

pa = '/home/www/aaa.txt'
pa1 = 'wang.py'
print("文件名："+os.path.basename(pa))      #basename,返回文件目录文件名
print("目录："+os.path.dirname(pa))        #dirname  返回目录

info = os.path.split(pa)                    #os.path.split() 将目录和文件名分开。并放入元组中
print(info)

path2 = os.path.join('/','home','var','www','sss.txt')
print(path2)

#print(os.path.exists(pa))
if os.path.exists(pa1):                 #os.path.exists(path) 存在返回真，不存在返回false
    print(os.path.basename(pa1)+'存在')
else:
    print('nonono')
#print(os.path.exists(pa1))

if os.path.isfile(pa1):                 #os.path.isfile(path) 是否是一个文件，同理 还有isdir
    print('yes')

else:
    print('nnn')

aaa = time.localtime(os.path.getatime(pa1))         #os.path.getmtime(pa1) 返回修改时间，getatime 返回读取时间
bbb = time.localtime(os.path.getctime(pa1))         #os.path.getctime(pa1) 返回该文件的创建时间  时间戳
print(datetime.datetime(aaa.tm_year,aaa.tm_mon,aaa.tm_mday,aaa.tm_hour))
print(datetime.datetime(bbb.tm_year,bbb.tm_mon,bbb.tm_mday,bbb.tm_hour))

print(glob.glob('e:/*'))            #列出E盘所有文件 类似于linux  ls命令

