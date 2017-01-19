# 魔法方法|__new__,__init__

class Rectangle:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def getPeri(self):
		return (self.x+self.y)*2
	def getArea(self):
		return self.x*self.y

rect=Rectangle(3,4)
print(rect.getPeri())
print(rect.getArea())

# __init__一般不做任何返回
# __new__很少做重写

class CapStr(str):
	def __new__(cls,string):
		string=string.upper()
		return str.__new__(cls,string)

a=CapStr('I Love You')
print(a)

# 垃圾回收机制，没有任何变量引用的时候，Python会自动调用__del__方法

class C:
	def __init__(self):
		print('I am __init__')
	def __del__(self):
		print('I am __del__')

c1=C()
c2=c1
c3=c2
del c3 # 当对象生成后，所有对它的引用都被del之后才会调用垃圾回收机制
