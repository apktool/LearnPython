# 函数|递归(factorial,Fibonacci)

# 求解factorial
def MyFunction(n):
	if n==1:
		return 1
	return n*MyFunction(n-1)

temp=MyFunction(5)
print(temp)

# 求解Fibonacci sequence
def Feber(x):
	if x==1 or x==2:
		return 1
	return Feber(x-1)+Feber(x-2)

print(Feber(20))
