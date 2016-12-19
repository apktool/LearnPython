"""
random,while
"""
#--coding:utf-8--
import random
secret=random.randint(1,10)
print("---------------------Hello world---------------")
guess=0
cnt=3
while guess!=secret and cnt!=0:
	tmp=input("input the number:")
	guess=int(tmp)

	if guess==secret:
		print("The number that you input is right")
	if guess<secret:
		print("small")
	if guess>secret:
		print("large")

	cnt-=1
print("end");
