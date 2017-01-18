# 内置函数|BIF

class A:
	pass

class B(A):
	pass

print(issubclass(B,A)) # B是否是A的派生类，如果是，返回True

a=A()
b=B()
print(isinstance(a,A)) # 检查一个对象是不是某个类的实例
print(isinstance(b,A))

class C:
	def __init__(self,x=0):
		self.x=x

c=C()

print(hasattr(c,'x')) # 测试一个对象是否有想要测试的属性
print(getattr(c,'y','No attribute you want to know'))# 返回对象指定的属性值，如果不存在，则抛出异常。如果设置了默认值，则返回默认值
print(setattr(c,'y','The attribute will be build'))# 设置对象中指定对象的值，如果不存在，则创建并且赋值
print(delattr(c,'y')) # 删除对象中的属性，如果对象中的属性不存在，则抛出AttributeError异常

# 通过属性设置属性

class D:
	def __init__(self,size=10):
		self.size=size
	def getSize(self):
		return self.size
	def setSize(self,value):
		self.size=value
	def delSize(self):
		del self.size
	x=property(getSize,setSize,delSize)

# property(获取属性的方法，设置属性的方法，删除属性的方法)

d=D()
d.getSize()
print(d.x)
d.x=18
print(d.size)

del d.x
print(d.size)
