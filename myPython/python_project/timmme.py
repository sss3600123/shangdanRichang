import time
import datetime
print(time.time())          #返回一个时间戳
#time.sleep(10)              #睡眠10秒 同时下边的代码不执行。直到睡眠结束
print(time.time())

print(time.gmtime())        #返回一个UTC时间对象
c_t = time.localtime(time.time())
print(c_t.tm_year,c_t.tm_mon,c_t.tm_mday)
print(time.localtime())     #返回一个本地区时间对象
print(time.mktime(time.localtime()))        #将对象转换为时间戳
print('----------------')
print(datetime.datetime(2015,12,3,11,55,5))     #返回时间这样的格式 2015-12-03 11:55:05



t1 = datetime.datetime(2015,12,3,13,39,00)
tt = datetime.timedelta(seconds = 55)           #时间相加
tt2 = datetime.timedelta(days = 10)             #时间间隔
print(t1+tt)
print(t1 + tt2)


print(datetime.datetime(c_t.tm_year,c_t.tm_mon,c_t.tm_mday,c_t.tm_hour,c_t.tm_min,c_t.tm_sec))

print(time.localtime())