# 类的继承
class people(object):
    def __init__(self):
        pass

    def display(self):
        print('hello word')


class manager(object):
    def __init__(self, people = None, name='li', sex='male', age=24):
        self._People = people
        self._Name = name
        self._Sex = sex
        self._Age = age

    def display(self):
        print('+++++')
        print(self._People.display())  # 此处有疑问,打印None
        print('+++++')
        print(self._Name)
        print(self._Sex)
        print(self._Age)


class student(people):
    def __init__(self, name='wang', sex='female', age=25):
        self._Name = name
        self._Sex = sex
        self._Age = age
        super().__init__()  # 注意super()与其他属性的顺序
        super().display()

    def display(self):
        print(self._Name)
        print(self._Sex)
        print(self._Age)


b = people()
a = manager(b, 'wengang', 'female', 10)
a.display()
print('---------------------')
d = student('xiaoxiao', 'male')
d.display()
