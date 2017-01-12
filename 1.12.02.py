#--coding:utf-8

# 格式化字符串

tmp="{0} love {1}.{2}".format("I","google","com")
print(tmp)

tmp="{a} love {b}.{c}".format(a="I",b="google",c="com")
print(tmp)

tmp="{{}}".format("not print")
print(tmp)

tmp="{0:.1f}{1}".format(27.658,"GB")
print(tmp)

# 格式化输出

tmp="%c" % 97
print(tmp)

tmp="%c %c %c" %(97,98,99)
print(tmp)

tmp="%s" % "I love you"
print(tmp)

tmp="%d+%d=%d" %(1,2,1+2)
print(tmp)

tmp="%o %x %X" %(15,15,15)
print(tmp)

tmp="%f %e %g" %(27.658,27.658,27.658)
print(tmp)

tmp="%#o" % 15 #以八进制打印输出
print(tmp)

tmp="%#d" % 15 #以十进制打印输出
print(tmp)

tmp="%#X" % 15 #以十六进制打印输出
print(tmp)
