# 正则表达式|findall

import re

url='<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=fd0005bcecdde711e7d243fe97eecef4/2160a218972bd4071d98664472899e510eb309eb.jpg" size="47010" width="421" height="750">'

modre=r'img class="BDE_Image" src="([^"]+\.jpg)"'

addr=re.findall(modre,url)
print(addr)

p=re.compile(modre)
addr=p.findall(url)
print(addr)

'''
findall
如果给定的正则表达式包括单个子组的话，会将该子组匹配到的内容单独返回
如果给定的正则表达包括多个子组的话，会将子组匹配到的内容组合成元组再返回

(?...)
正则表达式的扩展语法，可以避免使用findall方法的时候，由于子组所导致的错误
'''
