# lambda表达式
# 匿名函数

def ds(x):
	return 2*x+1

temp=ds(5)
print(temp)

###############################

temp=lambda x:2*x+1
print(temp(4))

###############################

temp=lambda x,y:x+y
print(temp(3,4))
