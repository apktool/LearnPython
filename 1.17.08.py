# 类|组合

class Turtle:
	def __init__(self,x):
		self.num=x

class Fish:
	def __init__(self,x):
		self.num=x

class Pool:
	def __init__(self,x,y):
		self.turtle=Turtle(x)
		self.fish=Fish(y)

	def print_num(self):
		print('There are %d tortoise, There are %d fishes'%(self.turtle.num,self.fish.num))

pool=Pool(1,10)
pool.print_num()

'''
组合是将不同的类混合并加入到其他类中，来增加类的功能/提高代码的重用性/易于维护(对类的修改会直接反应到整个应用中)。我们可以实例化一个更大的对象，同时还可以添加一些实例属性和实例方法的实现来丰富实例对象的功能。
子类会从基类继承他们的任何属性(数据和方法)，这种派生是可以继承多代的，且可以同时继承多个基类。
当我们派生一个子类，但同时希望相同的方法能在子类实现不同的功能，这时我们需要使用方法的 重载。使子类的方法能够覆盖父类的同名方法。
'''
