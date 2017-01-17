# 异常处理

try:
	sum=1+'1'
	f=open('Non.txt')
	print(f.read())
	f.close()
except(OSError,TypeError):
	print('error')
