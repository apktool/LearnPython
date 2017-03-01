# 多进程|multiprocessing

from multiprocessing import Pool

def f1(x):
    return x*x

with Pool(5) as p:
    print(p.map(f1,[1,2,3]))

#---------------------------------
print('---------------')
#---------------------------------

import multiprocessing
from multiprocessing import Pool as ThreadPool

def f2(x):
    print('%s -> %d'%(multiprocessing.current_process().name,x*x))

p=ThreadPool()
p.map(f2,range(10))
p.close()
p.join()

#---------------------------------
print('---------------')
#---------------------------------

from multiprocessing import Process

def f3(name):
    print('hello %s'%(name))

p=Process(target=f3,args=('Alice',))
p.start()
p.join()
