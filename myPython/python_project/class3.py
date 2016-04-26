#!/usr/bin/env python3
# -*- coding: utf-8  -*-
"""第一行，是为了在linux或max下 可以直接运行，当然。还有。chmod a+x 当前文件名  windows下是不可以用的。
   第二行是设置编码
"""
class asdef(object):
	def __init__(self):
		self.name = '123'
		self.age = 18

	def __s1(self):
		return self.name

	@property
	def s3(self):
		return self.__s1()

	def s2(self):
		return self.age

aa = asdef()
print(aa.s2())
print('你好世界')
print(aa.s3)
aaa = ['113','226','339']

for index in xrange(len(aaa)):
	print(aaa[index])

a2 = {'name':'ll','age':18,'sex':1}
if a2.get('sex',-1) == -1:
	#查看a2中是否存在 sex字段，不存在返回-1
	print('no exists')
else:
	print(a2.get('sex'))


#函数可以返回多个值
def moreval(x,y):
	nx = x + 5
	ny = y + 6
	return nx,ny

def morecc(a,b,*c,**d):
	print(a,b,c,d)

#morecc(1,2,3,4,x='ll',y='erw')
