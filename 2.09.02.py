# 多线程|lock

import threading,time

lock=threading.Lock()

balance=0

def change(n):
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for i in range(1000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()

t1=threading.Thread(target=run_thread,name='A',args=(5,))
t2=threading.Thread(target=run_thread,name='B',args=(8,))
t1.start()
t1.join()
t2.start()
t2.join()

print(balance)
