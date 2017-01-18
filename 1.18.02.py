# 构造函数和析构函数

class CapStr(str):
	def __new__(cls,string):
		string=string.upper()
		return str.__new__(cls,string)

a=CapStr('I Love You')
print(a)

#############

class C:
	def __init__(self):
		print('I am __init__')
	def __del__(self):
		print('I am __del__')

c1=C()
c2=c1
c3=c2
del c2
del c1
