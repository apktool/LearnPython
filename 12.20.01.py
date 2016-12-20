#--coding:utf-8--
import random
rand=random.randint(1,10)

cnt=5

print("-------hello world----------")
while cnt!=-0:
	tmp=input("Input the number: ")
	value=int(tmp)
	if(value==rand):
		print("right")
		break
	elif(value<rand):
		print("small")
	else:
		print("large")
	cnt-=1
print("end")
