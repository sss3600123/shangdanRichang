#coding:utf-8
import copy
import tkinter
import sys
import os
import time
import webbrowser
class MyCopy(object):
    def __init__(self,value):
        self.value = value


    def __repr__(self):             #将返回值变为字符串
        return str(self.value)

foo = MyCopy(7)
print(foo)
print(type(foo))

# a = ['foo',foo]
# b = a[:]
# print(a)
# print(b)
# c = list(a)
# print(c)
# d = copy.copy(a)
# e = copy.deepcopy(a)
# print('---------')
# print(d)
# print(e)
# print(copy.__all__)
# print('你好')
# top = tkinter.Tk()
# top.mainloop()

#sys.exit('end')
#print(dir(tkinter))
#print(dir(os))
#print(os.listdir(os.getcwd()))  #列出目录下所有的文件
# try:
#     #os.remove(os.getcwd()+'/aaa')        #删除文件
#     newpath = os.getcwd()+'/aaa/'
#     ff = os.listdir(newpath)
#     for i in ff:
#         os.remove(newpath+i)
#         print(i+' 删除成功')
# except Exception:
#     print('删除错误')
#os.makedirs('asd')          #创建dir
#os.chdir('asd')             #切换目录
# print(os.getcwd())
# cur_stat = os.stat(os.getcwd())
# print(time.ctime(cur_stat[8]))
# print(time.strftime('%Y-%m-%d %H:%M:%S'))       #返回一个格式化时间
#print(os.stat(os.getcwd()))             #查看当前目录的状态
#print(os.listdir(os.getcwd()))  #列出目录下所有的文件
# print(os.system('dir'))
# print('启动apache界面。。。')
#os.system(r"E:\Apache24\bin\ApacheMonitor.exe")     #可以是dos命令，可以启动某个程序 用r'',转义，
#webbrowser.open('http://www.163.com')            #浏览器库.可打开网页


