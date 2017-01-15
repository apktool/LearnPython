# 函数|递归（hanoi）

def hanoi(n,x,y,z):
	if n==1:
		print(x,'->',z)
		return
	else:
		hanoi(n-1,x,z,y)
		print(x,'->',z)
		hanoi(n-1,y,x,z)

temp=input("Please input the number of level: ")
n=int(temp)
hanoi(n,'a','b','c')
