print 'How old are you',
age=raw_input()
print 'How tall are you',
height=raw_input()
print 'How much do you weigh',
weight=raw_input()
print "So, you're %r old, %r tall and %r heavy." %(age,height,weight)

age=raw_input('How old are you ')
height=raw_input('How tall are you ')
weight=raw_input('How much do you weigh ')
print "So, you're %r old, %r tall and %r heavy." %(age,height,weight)

#python 7.12.01.py secondvariable
from sys import argv
script, first=argv
print "The script is called:",script
print "The first variable is:",first

#读取文件并打印
from sys import argv
script,filename=argv
txt=open(filename);
print "Here's your file %r:"%filename
print txt.read()
