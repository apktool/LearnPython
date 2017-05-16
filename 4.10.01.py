# @property

class C(object):
    def __init__(self):
        self._x = None
    def getx(self):
        print('What the fuck?')
        return self._x

    def setx(self, value):
        print('Why do you try to setting?')
        self._x = value

    def delx(self):
        print('Oh, shit, You can\'t delete me!')
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

class D(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


if __name__ == '__main__':
    c=C()
    c.x='hello world'
    print(c.x)
    del c.x

    d=D()
    d.x='hello python3'
    print(d.x)
    del d.x

"""
类C和类D是等价的，只是不同的表示方法而已。

个人对property的理解：
如果不使用property内置函数的话也是可以完成基本功能的，但是比如
c.x='hello world'
不使用propery，它仅仅可以完成对属性的赋值操作。但是使用property的时候，会进入setx函数，进行操作，如果有需求的话，完全可以在setx完成其他需求的初始化工作，而对外仅仅只需要
c.x='hello world'
这个简单的操作就可以，极好的封装了内部的其他操作。
"""
