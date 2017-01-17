# class|__init__

class Ball:
	name='ABC'
	__name='DEF' #类似于C++的私有属性
	def __init__(self,name='None'):
		self.name=name
	def kick(self):
		print('%s'%self.name)

a=Ball()
a.kick()

a=Ball('A')
a.kick()

print(a.name)
print(a._Ball__name)
# print(a.__name)

'''
Python的私有属性前面加'__'即可；
但是应该注意到Python的私有属性是一种伪私有，通过外部仍然可以访问
'''
