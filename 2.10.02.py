# 正则表达式

import re

content='010-1234'
temp=re.match(r'^\d{3,4}\-\d{3,8}$',content) 
print(temp)

if temp!=None:
    print('True')
else:
    print('False')

print('------------')

str1=temp=re.split(r'\s+','a b  c  d')
print(temp)

temp=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(temp.group(0))
print(temp.group(1))
print(temp.group(2))

time='16:32:35'
temp=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', time)
print(temp.group())
