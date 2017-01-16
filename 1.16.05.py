# 异常处理|try,except,finally

# 如果不加finally的话，因为写入之后，执行sum发生异常，直接抛出异常而导致文件不能正常写入，因此追加finally强制执行

try:
	f=open('haha.txt','w')
	print(f.write('I exist!'))
	sum=1+'1'
except(OSError,TypeError):
	print('error')
finally:
	f.close()
