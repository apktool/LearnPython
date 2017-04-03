# 调用父目录module的方法

# __init__.py
'''
from config import config
a = config()
a.printf()
print('hello init | %s' % __name__)
'''

# config.py
'''
class config(object):
    def printf(self):
        print('hello config | %s' % __name__)
'''

# main.py
'''
import app
'''

# 目录结构
'''
main.py
config.py
app
└── __init__.py
'''

# 运行方式
'''
python3 main.py
'''

'''
python中单纯的调用父目录中的module，而不指明路径是不可能的，因此可以考虑将其做成package，即在package中调用父目录的module，然后在父目录的另一个文件中调用package
'''
