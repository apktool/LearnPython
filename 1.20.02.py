# 获取当前目录下的sound和tcp文件夹中的所有内容，并将其目录改到指定目录下面

import os
import os.path

def get_data_files(data_dirs,prefix):
    data_files=[]
    for directory in data_dirs:
        for dir_path,_,file_names in os.walk(directory):
            target_dir=os.path.join(prefix,directory)
            local_files=[os.path.join(dir_path,f) for f in file_names]
            data_files.append((target_dir,local_files))
    return data_files


data_files=get_data_files(['sound','tcp'],'/home/li')
print(data_files)
