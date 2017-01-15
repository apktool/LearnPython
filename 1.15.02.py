# 过滤器|filter

temp=filter(None,[1,0,False,True])
print(list(temp))

############################

def odd(x):
	return x%2

num=(2,4,0,12,11)
temp=filter(odd,num)
print(list(temp))

############################

temp=filter(lambda x:x%2,range(10))
print(list(temp))
