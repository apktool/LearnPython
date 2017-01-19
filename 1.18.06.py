# 自定义装饰器

import time

def foo():
    print('I am foo()')

def timeit(func):
    def wrapper():
        start=time.clock()
        func()
        end=time.clock()
        print('used:%f'%(end-start))
    return wrapper

foo=timeit(foo)
print(foo())

'''
我们只需要在定义foo以后调用foo之前，加上foo = timeit(foo)，就可以达到计时的目的，这也就是装饰器的概念，看起来像是foo被timeit装饰了。在在这个例子中，函数进入和退出时需要计时，这被称为一个横切面(Aspect)，这种编程方式被称为面向切面的编程(Aspect-Oriented Programming)
'''

# python语法糖|对装饰器的额外支持

@timeit
def haha():
    print('I am haha')

print(haha())
