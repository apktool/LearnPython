# 魔法方法|相关属性|__getattribute__,__getattr__,__setattr__,__delattr__

class C:
	def __getattribute__(self,name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self,name):
		print('getattr')
	def __setattr__(self,name,value):
		print('setattr')
		super().__setattr__(name,value)
	def __delattr_(self,name):
		print('delattr')
		super().__delattr__(name)
c=C()
print(c.x)

c.x=1
print(c.x)

del c
