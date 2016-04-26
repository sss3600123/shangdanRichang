#coding:utf-8
class News(object):
	def __init__(self,data):
		self.data = data
		
	def getdata(self):
		print(self.data)
		
	@classmethod
	def getdatac(*args):
		print("method")
		#print('classmethod:%s' % (self.data))
		
	@staticmethod
	def getdatas(*args):
		print('static')
		# print(self.data)
		

		
		
class Kls(object):
    def __init__(self, data):
        self.data = data
 
    def printd(self):
        print(self.data)
 
    @staticmethod
    def smethod(*arg):
        print('Static:', arg)
 
    @classmethod
    def cmethod(cls):
        print('Class:', cls)


nn = News('asd')
#nn.getdata()
#nn.getdatac()
#nn.getdatas()
#News.getdatac()
#News.getdatas()


ik = Kls(23)

ik.smethod()
ik.cmethod()

 # Kls.printd()

 # Kls.smethod()

 # Kls.cmethod()

