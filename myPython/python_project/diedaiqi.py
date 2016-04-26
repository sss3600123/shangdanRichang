#!/usr/bin/enc python
#coding:utf-8
#迭代器
aa = [1,2,3,4,5,6,7,8,9]
newaa = iter(aa)
for i in range(len(aa)):
    print('这是第%d个，值为：%d' % (i,newaa.__next__()))
