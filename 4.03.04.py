# 绝对导入，相对导入

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

'''
Imports: Multi-Line and Absolute/Relative
https://www.python.org/dev/peps/pep-0328/


A single leading dot indicates a relative import, starting with the current
package. Two or more leading dots give a relative import to the parent(s) of
the current package, one level per dot after the first. 

Relative imports must always use from <> import ; import <> is always absolute.
Of course, absolute imports can use from <> import by omitting the leading dots. 
'''
