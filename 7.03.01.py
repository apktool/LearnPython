age=16
if age>=18:
	print 'adult'
elif age>15 and age<18:
	print 'teenger'
else:
	print 'kid'
print 'hello process end'

L=[75,92,59,68]
sum=0.0
for score in L:
	sum+=score
print sum/4.0

N=10
x=0
while x<N:
	x+=3
print x

sum=0
x=1
n=1
while True:
	sum+=x
	x*=2
	n+=1
	if n==21:
		break;
print sum

sum=0
x=0
while True:
	x=x+1
	if x>100:
		break
	if x%2==0:
		continue
	sum+=x
print sum

cnt=0
for i in [0,1,2,3,4,5,6,7,8,9]:
	for j in [0,1,2,3,4,5,6,7,8,9]:
		if i<j:
			cnt=i*10+j
			print cnt;
