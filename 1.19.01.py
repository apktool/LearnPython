# importlib的简单使用|importlib.import_module()

import importlib
import os.path

command_mod_name='pkg011901'
mod=importlib.import_module('package.'+command_mod_name)
mod.foo()

temp=mod.name_test()
print(temp)

'''
目录结构
./
package/
        ../
        pkg011901.py
'''

###################################

'''
# pkg011901.py

import time

def timeit(func):
    def wrapper():
        start=time.clock()
        func()
        end=time.clock()
        print('used:%f'%(end-start))
    return wrapper

@timeit
def foo():
    print('I am foo()')

def name_test():
    return 'haha'
'''
