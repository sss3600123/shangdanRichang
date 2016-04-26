#!/usr/bin/python
# -*- coding:UTF-8 -*-
import time,sys,math;
def printme( str ):
    print(str)
    return
printme("调用")
print(time.localtime(time.time()))

a = [66.25,33,55,88,66,33]
print(a)
print(len(a))
print(a[0])
print(a[1:3])
#for i in range(len(a)):
    #print(a[i])

#print(a.count(33))          #33在list 中出现的次数
print(sys.path)
print(dir())
print("{0} and {1}".format('tom','jelly'))
print("%.8f" % math.pi)
f = open(sys.path[0]+"\\aaa.txt","r+")
#print(f.readline())


with open(sys.path[0]+"\\aaa.txt","r+") as f:
    f.write('ddddddd')
    print(f.read())
f.closed