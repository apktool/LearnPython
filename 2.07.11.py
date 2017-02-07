# 生成器

def myGen():
	print('生成器正在被执行')
	yield '暂停成功1'
	yield '暂停成功2'

my=myGen()

print(next(my))
print(next(my))

print('-->')

def libs():
	a=0
	b=1
	while True:
		a,b=b,a+b
		yield a

for each in libs():
	if each > 100:
		break;
	print(each,end=' ')
