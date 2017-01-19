#!/usr/bin/env python3

from distutils.core import setup
from distutils.command.install import install
from distutils.command.build import build
from distutils.command.config import config
import os.path
import glob

class _override_install(install):
    def run(self):
        print('haha, I am installing')
        #install.run(self)

class _override_build(build):
    def run(self):
        print('ahah, I am building')
        build.run(self)

class _override_config(build):
    def run(self):
        print('hhaa, I am configing')
        config.run(self)

if __name__=='__main__':
    setup(
        name='setup test',
        version='1.0',
        author='apktool',
        scripts=glob.glob('./1.18.06.py'),
        cmdclass={'install':_override_install,
            'build':_override_build,
            'config':_override_config},
    )

'''
setup.py的简单实现
使用方法|命令无先后顺序:
./1.19.03.py config
./1.19.03.py build
./1.19.03.py install
'''
