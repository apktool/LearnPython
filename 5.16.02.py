# __file__

print(__file__)

'''
注意:
python3 /home/li/WorkSpace/LearnPython/5.16.02.py
结果是
/home/li/WorkSpace/LearnPython/5.16.02.py

python3 5.16.02.py
结果是
5.16.02.py

python3 ../LearnPython/5.16.02.py
结果是
../LearnPython/5.16.02.py
'''

import flask
print(flask.__file__)
'''
结果是
/usr/local/lib/python3.6/site-packages/flask/__init__.py
'''

"""
__file__ is the pathname of the file from which the module was loaded.
if it was loaded **from a file**. The __file__ attribute is not present for C modules that are statically link to interperter;
for extension modules loaded dynamical **from a shared library**, it is the pathname of the shared library file.
"""
