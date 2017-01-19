# 魔法方法|算数运算|__add__,__sub__,__rand__,__sub__

class New_int(int):
	def __add__(self,other):
		#return int(self)+int(other)
		return int.__sub__(self,other)
	def __sub__(self,other):
		#return int(self)-int(other)
		return int.__add__(self,other)
		
a=New_int(3)
b=New_int(5)
print(a+b)
print(a-b)

'''
self可以认为是类的实例化绑定的一个对象
'''

class Nint(int):
	def __rand__(self,other):
		return int.__sub__(self,other)



a=Nint(5)
b=Nint(3)
print(a+b) #8
print(1+b) #2
print(3-a) #-1

class Nint(int):
	def __rsub__(self,other):
		#return int.__sub__(self,other)
		return int.__sub__(other,self)

a=Nint(5)
print(3-a) #-2
