# 文件操作

f=open('README.md')
#print(f.read())

f.seek(0)

temp=f.readline()
print(list(temp))

f.close()
