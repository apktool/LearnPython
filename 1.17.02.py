# 异常处理|try,except,else

try:
	int('abc')
except ValueError as reason:
	print('error'+str(reason))
else:
	print('normal')
