# -*- coding:utf-8 -*-

def ff():
    global s
    print(id(s))
    s = "hello world"
    print(s)


s = "I am looking for a course in Paris!"
print(id(s))
ff()
print(s)
