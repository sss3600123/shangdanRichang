from datetime import datetime
'''
这是datetime 模块
'''
#字符串转时间
cday = datetime.strptime('2016-1-27 9:23:15','%Y-%m-%d %H:%M:%S')
print(cday)
print('---------------')
#当前时间
print(datetime.now())
print('时间戳')
#时间戳
print((datetime.now()).timestamp())
