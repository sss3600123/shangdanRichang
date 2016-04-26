import os;
class myClass:
    """这是一个类,__init__为构造方法。每个方法的参数都是self，相当于php中的$this"""
    #i = 1245
    def __init__(self,num1,num2):
        self.i = 5555
        self.i1 = num1
        self.i2 = num2
    def f(self):
        return 'hello world'
    def hh(self):
        print("和为：" + repr(self.i1+self.i2))
    def getcwd(self):
        print(os.getcwd())

x = myClass(11,22)
print(x.f())
print(x.i)
print(x.i1)
print(x.i2)
x.hh()
x.getcwd()