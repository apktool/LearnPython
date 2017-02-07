# fork(),getpid(),getppid()

import os

print('%s'%os.getpid())

pid=os.fork()

if pid==0:
    print('Child: %s'%(os.getpid()))
else:
    print('Parent: %s'%(os.getpid()))
