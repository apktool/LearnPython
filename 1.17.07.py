# 类|多重继承

class Base1:
	def foo1(self):
		print("foo1|Base1")

class Base2:
	def foo2(self):
		print("foo2|Base2")

class C(Base1,Base2):
	pass

c=C()
c.foo1()
c.foo2()
