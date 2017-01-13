#--coding:utf-8--

# 函数|不带参函数，带参函数

def MyFirstFunction():
	print("hello world")

MyFirstFunction()

def MyScondFunction(name):
	'这里是函数文档，应该不会显示在屏幕上'
	# 这里name只是一个形式，表示占据一个参数位置
	print('传递进来的'+name+'叫做实参，因为Ta是具体的参数值')
	# 打印函数文档
	print(MyScondFunction.__doc__)

MyScondFunction('aron')

def sum(num1, num2):
	result=num1+num2
	print(result)

sum(3,4)

def sub(num1, num2):
	return num1-num2

c=sub(5,4)
print(c)
