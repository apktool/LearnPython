# 魔法方法|基本魔法方法|__str__,__repr__

class A():
	def __str__(self):
		return 'haha'

a=A()
print(a)

class B():
	def __repr__(self):
		return 'ahah'

b=B()
print(b)
