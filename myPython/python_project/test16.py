# coding: utf-8

#def aa(arg1,arg2,**arg3):
    #print("name:%s,age:%d,other:%s" % (arg1,arg2,arg3))

#aa('ll',23,city="上海")


def person(name,age,**kw):
    print("name:%s,age:%d,other:%s"%(name,age,kw))

person('陈',23)
person('陈',23,city="武汉")
