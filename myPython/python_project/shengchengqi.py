#!/usr/bin/env python
#coding:utf-8
#生成器

def cash_out(amount):
    while amount > 0:
        amount -= 1
        yield amount
        print('擦，又来取钱了。。。败家子')

atm = cash_out(3)
print('取到钱%s万' % (atm.__next__()))
print('化掉划掉')
print('取到钱%s万' % (atm.__next__()))
print('取到钱%s万' % (atm.__next__()))

'''
调用流程：
1.atm = cash_out(3) 这个没有输出，只是一个生成器，只有在next的时候才会输出
2. 第一次 print('取到钱%s万' % (atm.__next__()))，这个时候会返回1，生成器作用显示，返回1后，底下的代码不执行，，只有下次调用的时候。先返回‘取钱’,再返回1，，一次类推
生成器的作用，每次调用返回一个，同时，函数会在返回后中断，下次调用是，从中断楚代码开始执行，有返回数字，依次类推
'''


atm1 = cash_out(5)
while True:
    try:
        print(atm1.__next__())

    except StopIteration as e:
        print('循环完了')
        break


atm2 = cash_out(7)
for i in atm2:
    print(i)
