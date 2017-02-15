# 正则表达式|基本语法

import re

p=re.compile(r'(baidu)\1')
temp=p.search('baidubaidu')
print(temp)

'''
(baidu)\1 实际上等价于 baidubaidu
这里 \1 的意思是代表 第1组 .或者说将第1组再写一遍
'''

p=re.compile(r'(baidu)\141')
temp=p.search('baidua')
print(temp)

'''
\141 这里的意思是字符a，为a的ASCII码的八进制表示
\数字
如果数字以0或者3位数字长度，则不会被用于引用对应的子组，而是用于匹配八进制数字所表示的ASCII吗值对应的字节
'''

p=re.compile(r'[^a-z]')
temp=p.findall('www.BaiDu.com')
print(temp)

p=re.compile(r'[a-z^]')
temp=p.findall('www.BaiDu.com^')
print(temp)

'''
^ 放在表达式的最前面表示取反
^ 放在表达式的后面表示自身
'''

p=re.compile(r'https?.+\.html')
temp=p.search('https://www.baidu.com/xy/123.html')
print(temp)

'''
.+ 注意这种灵活用法，可以表示匹配任意字符
'''

p=re.compile(r'<.+?>')
temp=p.search('<html><title>I love You<title><html>')
print(temp)

'''
这里的?表示取消贪婪匹配模式
'''

'''
元字符
. ^ $ * + ? { } [ ] ( ) \ |
'''
