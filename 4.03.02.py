# 简单工厂模式
class HaHa(object):
    def __init__(self, name):
        self.name = name

    def fun(self):
        print('Hello %s' % self.name)


def create_fun(name):
    app = HaHa(name)
    return app


app = create_fun('Apktool')
temp = app.fun()

'''
工厂模式：源于模式设计中的一种方法，就是指不通过类来直接构造对象，而是通过一个函数来构造对象。
这样允许你在函数中加入更多的控制

工厂模式按照《Java与模式》中提法分为三类
- 简单工厂模式(Simple Factory)
- 工厂方法模式(Factory Method)
- 抽象工厂模式(Abstract Factory)
'''
