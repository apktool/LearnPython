# from .main import **

from app import Haha
a = Haha().fun()

# 目录结构
'''
4.03.04.py
app
├── __init__.py
└── main
    └── __init__.py
'''

# 4.03.04.py
'''
import app
app.Haha().fun()
'''

# app/__init__.py
'''
from .main import Haha
print(__name__)
'''

# app/main/__init__.py
'''
class Haha(object):
    def __init__(self):
        pass

    def fun(self):
        print('hello world')
        print(__name__)
'''

'''
注意：
from main import Haha 和 from .main import Haha
是不一样的。
.main 一般用在package的内部导入里面

from .main import Haha 更类似与 from app.main import Haha
'''
