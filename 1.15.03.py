# 函数|递归

def MyFunction(n):
	if n==1:
		return 1
	return n*MyFunction(n-1)

temp=MyFunction(5)
print(temp)
