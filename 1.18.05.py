# 装饰器|@property

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter # 这里定义的属性是一个只读属性，如果需要可写，则需要再定义一个setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be integer')
        if value<0 or value>100:
            raise ValueError('score must between 0 and 100')
        self._score=value

s=Student()
s.score=60
print(s.score)

'''
内置的装饰器有三个，分别是staticmethod、classmethod和property，作用分别是把类中定义的实例方法变成静态方法、类方法和类属性。
'''
