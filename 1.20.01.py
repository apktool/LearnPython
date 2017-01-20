# setup.py文件install之个人猜想

# 主要采用的是继承机制

class A(object):
    def __init__(self):
        self.run()
    def run(self):
        print('I am A, I am running')
    def walk(self):
        print('I am A, I am walking')


class B(A):
    def run(self):
        print('I am B, I am running')
        self.walk()

b=B()
