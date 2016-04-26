#!/usr/bin/env python
#coding:utf-8
#尽量不用+连接字符串。
print('hello %s, happy %s' % ('xiaolong','new year!'))

#交换赋值
a = 1
b = 2
print(a,b)

a,b = b,a
print(a,b)

_as = input('请输入关键词')
if _as == 'a':
    print('欢迎你，%s' % (_as))

else:
    print('翻滚吧，%s' % (_as))
