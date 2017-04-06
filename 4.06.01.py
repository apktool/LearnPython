# 常用的正则表达式

import re


# 匹配IP地址格式，但不保证IP地址合法
string = 'haha192.168.1.1heh'
r = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
temp = r.search(string)
print(temp.group())

# 匹配IP地址格式，保证IP地址合法
string = 'haha192.122.1.1heh'
# r = re.compile(r'((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)')
r = re.compile(r'((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}\2')
temp = r.search(string)
print(temp.group())


# 匹配EMAIL地址
string = 'example@domain.com'
# r = re.compile(r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}')
r = re.compile(r'\w+@\w+\.+[A-Za-z]{2,14}')
temp = r.search(string)
print(temp.group())


# 匹配中文字符
string = 'hello, 小王, hello python'
r = re.compile(r'[\u4e00-\u9fa5]+')
temp = r.search(string)
print(temp.group())

'''
http://deerchao.net/tutorials/regex/regex.htm
[a-z0-9A-Z_]完全等同于\w
'''
