# 集合|set

num={1,2,3,4,5,6}
print(num)

num={1,2,2,2,2,3,5,4,2,4}
print(num)

'''
set
set里面的元素必然唯一
set里面的元素无序
'''

set1=set([1,2,3,4,5,5,5,5,5]) #工厂函数 
print(set1)

set1.add(6)
print(set1)

set1.remove(5)
print(set1)

# 不可变集合|frozenset

num=frozenset([1,2,3,4,5])
print(num)
