# os|abspath,dirname

import os

temp=os.path.abspath('1.16.02.py')
print(temp)

# 打印文件所在目录名称：
#   如果传进来的是相对路径，输出空目录
#   如果传进来的是绝对路径，输出绝对路径和目录名称

temp=os.path.dirname('1.16.02.py')
print(temp)

temp=os.path.dirname('/home/li/Workspace/LearnPython/1.16.02.py')
print(temp)

# 显示1.16.02.py所在的目录名称

temp=os.path.dirname(os.path.abspath('1.16.02.py'))
print(temp)

# 显示1.16.02.py所在目录的目录的名称

temp=os.path.dirname(os.path.dirname(os.path.abspath('1.16.02.py')))
print(temp)
