# 类的属性访问

class C:
	def __init__(self):
		self.x='init'

# getattr()若对象c中有x属性，则返回x属性；若对象c中没有x属性，则返回定义的字符

c=C()
temp=getattr(c,'x','no have the attrbute')
print(temp)
temp=getattr(c,'y','no have the attrbute')
print(temp)

class D:
	def __init__(self,size=0):
		self.size=size
	def getSize(self):
		return self.size
	def setSize(self,value):
		self.size=value
	def delSize(self):
		del self.size
	x=property(getSize,setSize,delSize)

d=D()
print(d.x)
print(d.size)
del d.x
