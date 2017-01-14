# 函数局部变量和全局变量

count=5

def MyFun1():
	count=10
	print('Locality Parameter:',count)

print('Global Parameter:',count);
MyFun1()

##########################################

cnt=8
def MyFun2():
	global cnt
	cnt=88
	print('Modified by locality:',cnt)

print('Global Parameter:',cnt)
MyFun2()
