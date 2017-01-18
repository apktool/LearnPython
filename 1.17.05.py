# 类|继承

class Parent:
	def hello(self):
		print('Parent class')

class Child1(Parent):
	pass

p=Child1()
p.hello()

class Child2(Parent):
	def hello(self):
		print('Child class')

p=Child2()
p.hello()
