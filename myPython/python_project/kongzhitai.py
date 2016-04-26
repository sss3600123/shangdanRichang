#!/usr/bin/env python
#coding:utf-8

newdic = {'a':{'phone':'1666666666','name':'tt'},'b':{'phone':'17777777','name':'qq'},'c':{'phone':'1333333','name':'rrr'}}

while True:
    inp = input('请输入查询的号')
    if inp in newdic.keys():
        print('当前用户的电话为：%s,名字为：%s' %  (newdic[inp]['phone'],newdic[inp]['name']))

    elif inp == 'exit':
        print('谢谢使用\n')
        break
    else:
        print('输入有误\n')
