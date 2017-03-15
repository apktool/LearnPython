# 命名空间的访问

def func1(x, z):
    y = 12345
    print(locals())  # 局部命名空间
    locals()['y']=98765
    print(locals())
func1(1 , "first")

r='hello world'
print(globals())  # 全局(模块级别)命名空间

globals()['r']='hello python'
print(globals())

'''
locals 实际上没有返回局部名字空间，它返回的是一个拷贝。所以对它进行改变对局部名字空间中的变量值并无影响。
globals 返回实际的全局名字空间，而不是一个拷贝。所以对 globals 所返回的任何的改动都会直接影响到全局变量。
'''
