# 函数|内部函数（内嵌函数）

def fun1():
	print('fun1()正在被调用...')
	def fun2():
		print('fun2()正在被调用...')
	fun2()

fun1()

'''
注意：
fun2()的作用域在fun1()的函数里面，因此在fun1()的外面不能调用fun2()
'''
