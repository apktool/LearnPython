# try,except,with

try:
	with open('data.txt','w') as f:
		for each_line in f:
			print(each_line)
except OSError as reason:
	print('wrong'+str(reason))

'''
with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。
'''
