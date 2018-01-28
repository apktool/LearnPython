
class A(object):
    def __new__(cls, *args, **kwargs):
        print('A __new__')
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print('A __init__')

    def haha(self):
        print("Hello A")

class B(A):
    def __new__(cls, *args, **kwargs):
        print('B __new__')
        return A.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print('B __init__')

    def haha(self):
        print("Hello B")

b = B()
b.haha()

'''
__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。
__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。

也就是，__new__在__init__之前被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。


在定义子类时没有重新定义__new__()时，Python默认是调用该类的直接父类的__new__()方法来构造该类的实例，如果该类的父类也没有重写__new__()，那么将一直按此规矩追溯至object的__new__()方法，因为object是所有新式类的基类。
'''
