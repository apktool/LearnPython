# 命名空间的生命周期

x=1
def fun1():
    x=x+1
fun1()

def fun2():
    y=123
    del y
    print(y)
fun2()

'''
UnboundLocalError: local variable 'x' referenced before assignment
UnboundLocalError: local variable 'y' referenced before assignment
'''

'''
不同的命名空间在不同的时刻创建，有不同的生存期。
1、内置命名空间在 Python 解释器启动时创建，会一直保留，不被删除。
2、模块的全局命名空间在模块定义被读入时创建，通常模块命名空间也会一直保存到解释器退出。
3、当函数被调用时创建一个局部命名空间，当函数返回结果 或抛出异常时，被删除。每一个递归调用的函数都拥有自己的命名空间。
Python 的一个特别之处在于其赋值操作总是在最里层的作用域。赋值不会复制数据——只是将命名绑定到对象。删除也是如此："del y" 只是从局部作用域的命名空间中删除命名y。事实上，所有引入新命名的操作都作用于局部作用域。
'''
