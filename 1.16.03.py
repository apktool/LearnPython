# 异常处理

# try一旦检测到异常，后序代码将不会执行

try:
	sum=1+'1'
	f=open('Non.txt')
	print(f.read())
	f.close()
except OSError as reason:
	print('failed file, the reason is',reason)
except TypeError as reason:
	print('error type, the reason is ',reason)
