# getopt|命令行参数解析

import getopt,sys

args='-a -b -cfoo -d bar a1 a2'.split()
print(args)

optlist,args=getopt.getopt(args,'abc:d')

print(optlist)
print(args)


print('------------------')

s = '--condition=foo --testing --output-file abc.def -x a1 a2'
args=s.split()
print(args)

optlist,args=getopt.getopt(args,'x',['condition=','output-file=','testing'])

print(optlist)
print(args)

'''
“abc:d”
短格式 --- a b 后面没有冒号：表示后面不带参数，c：后面有冒号表示后面需要参数

["condition","output-fiel=","testing="]
长格式 --- help后面没有等号=，表示后面不带参数
'''
