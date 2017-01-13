#--coding:utf-8--

# 函数|关键字参数，默认参数，可变参数

#关键字参数，为了防止函数顺序混乱所导致的错误

def MyFirstFunction(name,words):
	print(name+'->'+words)

MyFirstFunction('Li','helloworld')
MyFirstFunction(words='haha',name='kang') 

#默认参数

def MyScondFunction(name='li',words='default'): 
	print(name+'->'+words)

MyScondFunction()
MyScondFunction('wang')
MyScondFunction('zhao','Modified')

#可变参数

def MyThirdFunction(*params):
	print('参数长度是:',len(params))
	print('第二个参数是:',params[1])

MyThirdFunction(1,2)
MyThirdFunction(1,2,3)
