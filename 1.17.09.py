# 类|绑定

class C:
	def x(self):
		print('x-man')

c=C()
c.x()

c.y=1
print(c.y)

#####################

class CC:
	def setXY(self,x,y):
		self.x=x
		self.y=y
	def printXY(self):
		print(self.x, self.y)

dd=CC()
print(dd.__dict__)
print(CC.__dict__)

'''
类的属性和方法同名的时候，会导致类的属性会覆盖方法从而导致调用出错
实例化
'''

'''
类定义              C
                    |
类对象              C
          |---------|----------|
实例对象  a         b          c
'''
