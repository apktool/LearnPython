# 绑定属性，方法,__slots__

from types import MethodType

class Students(object):
    pass

s=Students()
s.name='Michael' # 动态给实例绑定属性
print(s.name)

def set_age(self,age):
    self.age=age

s.set_age=MethodType(set_age,s) # 给实例绑定一个方法
s.set_age(25)
print(s.age)


def set_score(self,score):
    self.score=score

Students.set_score=set_score # 给类绑定一个方法
s=Students()
s.set_score(100)
print(s.score)

class Student(object):
    __slots__=('name','age')

c=Student()
c.name='Niki'
c.age=24
print(c.name,c.age)
try:
    c.score=100
except AttributeError as reason:
    print('Because \'__slots__\' is used to restricted atttribute defined | '+str(reason))

