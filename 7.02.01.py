# -*- coding: utf-8 -*-
print '\"hello\" \'world\''
print r'''
python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!
'''

'''
单行注释用#
多行注释可以使用三个单引号，但是注释中不能再出现三个连续的单引号
关于中文，如果在顶部不声明使用'utf-8'编码时，使用中文时，需要前面加u，表明该字符串是Unicode编码；
但是如果前面生命了编码打开方式，则无需再追加u标识符
'''

print u'我是中文'

print '''
静夜思
窗前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''

print 10+11
print 11.0/2

a='python'
print 'hello,',a or 'world'
print 'hello,',a and 'world'

b=''
print 'hello,',b or 'world'
print 'hello,',b and 'world'

#List是一种有序的集合，可以随时对元素增删改查
L=['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
print L
print L[0]
print L[1]

L.append('Li')
print L
L.insert(2,'wang')
print L
L.pop(2)
print L
L[6]='wang'
print L

#tuple术语“元祖”，一旦创建完毕便不能再次修改
t=(0,1,2,3,4,5,6,7,8,9)
print t
t=(0,)
print t
