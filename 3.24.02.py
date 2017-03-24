# 创建临时文件夹和临时文件

import tempfile

dirpath = tempfile.mkdtemp()
print(dirpath)

f = tempfile.NamedTemporaryFile(prefix='haha-', dir=dirpath, delete=False)
print(f.name)
