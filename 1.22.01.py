# get_outputs,os.path.split

import os.path
from distutils.core import setup
from distutils.command.install import install


class _OverrideInstall(install):
    def run(self):
        for install_file in self.get_outputs():
            print('->'+install_file)
            install_dir=os.path.split(install_file)[0]
            print('-->'+install_dir)
            install_dir=os.path.split(install_file)[1]
            print('-->'+install_dir)

setup(
        name='1.22.01',
        cmdclass={'install': _OverrideInstall},
    )
