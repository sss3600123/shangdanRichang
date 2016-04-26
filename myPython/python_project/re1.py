import re
a = '3sd45'
res = re.search('\d', a)        #只要有一致的，就可以
res1 = re.match('\d',a)         #match 首个要一直。否则返回None
print(res)
print(res.group(0))
print(res1)
print(res1.group(0))
ll = re.split('s',a)            #以第一个参数为分隔符。把第二个参数分割，返回一个list
ll2 = re.findall('\d',a)        #以一个参数匹配第二个参数。吧所有匹配成功的放入一个list中
print(ll2)
print(ll)

str = re.sub('\d','s',a)            #把出现的数字全部替换成s,并返回一个新的字符串
print(str)
# if res != None:
#     print(res.group(0))
# else:
#     if res1 != None:
#         print(res1.group(0))
#     else:
#         print('none1111')

mm = re.search('output_(\d{4})','output_1989.txt')
print(mm.group(0))              #grouop(0) 返回整个结果
print(mm.group(1))              #group(1) 返回第一个小括号里的


sss = "abad"
ll3 = re.split('a',sss)
print(ll3)



