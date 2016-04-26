#coding:utf-8
import glob
fileList = glob.glob('*.py5')		#获取所有符合条件的文件
if  fileList:
	for i in fileList:
		print(i)

else:
	print('No files list')
	
	
#解压序列赋值
newstr = 'asdfs'
# x,c,v,b,n = newstr
# print(x,c,v,b,n)	
'''这是测试'''
"""这是测试2"""
aaa = """这
是
测
试2"""
print(aaa)
sss = '''addg
fsd'''
print(sss)
# 三单引号或者三双引号 不赋值时可以当注释，赋值时可以原样输出，_表示占位
_,x,y,_,z = newstr	
print(x,y,z)

# 分割字符串

ssn = 'ewr:sgdgdf:frewrt:fsdfgdht:ergdfgdsad'
w,*args = ssn.split(':')
print(w)
print(args)

def sum(items):
	head,*tail = items
	return head + sum(tail) if tail else head
	

print(sum(['w','h','ere']))

print(range(3))
mylist = [x*x for x in range(5)]		#返回迭代返回x*x
for i in mylist:
	print(i)


