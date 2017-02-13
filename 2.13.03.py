# logging

import logging

'''
logging.basicConfig(filename='example.log',
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        level=logging.DEBUG)
'''
logging.getLogger('').setLevel(logging.DEBUG) # 这句不能少，如果缺少这句，会导致后面的setLevel不能正常工作

# 输出到控制台

formatter=logging.Formatter('(name)-12s: %(levelname)-8s %(message)s')

console=logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# 输出到文件

formatter=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

files=logging.FileHandler('example.log')
files.setLevel(logging.DEBUG)
files.setFormatter(formatter)
logging.getLogger('').addHandler(files)

# 日志等级及输出消息

logging.debug('I am debug message')
logging.info('I am info message')
logging.warning('I am warning message')
logging.error('I am error message')
logging.critical('I am critical message')

'''
默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
'''
