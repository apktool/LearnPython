# 类|实现继承的两种方式

import random as r

class Fish:
	def __init__(self):
		self.x=r.randint(0,10)
		self.y=r.randint(0,10)
	
	def move(self):
		self.x-=1
		print('Postion:',self.x,self.y)

class Goldfish(Fish):
	pass

class Carp(Fish):
	pass

class Salmon(Fish):
	pass

class Shark(Fish):
	def __init__(self):
		# Fish.__init__(self) #绑定父类的方法实现继承
		super().__init__() #使用super()实现继承
		self.hungry=True
	def eat(self):
		if self.hungry:
			print('Eating')
			self.hungry=False
		else:
			print('Not Eating')

fish=Fish()
fish.move()

shark=Shark()
shark.eat()
shark.move()

'''
调用为绑定的父类方法
使用super函数
'''
