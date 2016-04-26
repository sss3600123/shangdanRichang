# coding: utf-8
f = open("aaa.txt")
while True:
    str_line = f.readline()
    if len(str_line) == 0:
        break
    print(str_line)
