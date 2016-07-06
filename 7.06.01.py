# -*- coding: utf-8 -*-

L=[]
x=1
while x<=100:
	L.append(x*x)
	x+=1
print sum(L)

def square_of_sum(L):
	sum=0;
	for x in L:
		sum+=x*x
	return sum

print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])

import math
def move(x,y,step,angle):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx, ny

x,y=move(100,100,60,math.pi/6)
print x,y

def quadratic_quation(a,b,c):
	if (b*b-4*a*c)<0:
		return
	x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
	x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
	return x1,x2

x1,x2=quadratic_quation(2,3,0)
print x1,x2

#--------------------------------------------------

def move(n,a,b,c):
	if n==1:
		print a+'->'+c
		return
	move(n-1,a,c,b)
	print a+'->'+c
	move(n-1,b,a,c)

move(4,'A','B','C')

#--------------------------------------------------

def printhello(a='world'):
	print 'hello '+a

printhello()
printhello('Latex')

'''
可变参数也不是很神秘，Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，因此，在函数内部，直接把变量 args 看成一个 tuple 就好了。
'''
