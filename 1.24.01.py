# os.getcwd(),sys.path

import os
import sys

def append_path():
    pwd=os.getcwd()
    if pwd in sys.path:
        pass
    else:
        sys.path.append(pwd)

append_path()
