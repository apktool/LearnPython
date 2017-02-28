# 多进程|multiprocessing

from multiprocessing import Pool

def f1(x):
	return x*x

with Pool(5) as p:
	print(p.map(f1,[1,2,3]))

#---------------------------------
from multiprocessing import Process

def f2(name):
	print('hello %s'%(name))

p=Process(target=f2,args=('Alice',))
p.start()
p.join()
