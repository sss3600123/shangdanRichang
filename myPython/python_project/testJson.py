#coding:utf-8

import json
a = {"name":"ll","age":18,"checked":True,"address":None}
#将字典转化为json
newJ = json.dumps(a)
print("json:",newJ)
#将json转换为字典
newd = json.loads(newJ)
print("字典：",newd)
