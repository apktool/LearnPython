#!/usr/bin/python
import sys

def run():
    print('hello world')

print('Script\'s name: '+sys.argv[0])
for i in range(1,len(sys.argv)):
    if sys.argv[1]=='run':
        run()

'''
Python脚本的简单实现
使用时需要将本文件改名，因为本文件名非法，比如改成a.py
./a.py run
'''
