# map,reduce|实现将字符型数字转化为整形数字

from functools import reduce

def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

L=map(char2num,'78965')
print(list(L))

temp=reduce(fn, map(char2num, '13579'))
print(temp)
print(isinstance(temp,int))
