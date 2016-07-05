# -*- coding: utf-8 -*-
'''
dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。由于dict是按 key 查找，所以，在一个dict中，key不能重复。
dict的第二个特点就是存储的key-value序对是没有顺序的！
set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
'''
d={
	'Adam':95,
	'Lisa':85,
	'Bart':59,
	'Paul':75
}

print d['Adam']
print d.get('Lisa')
print 'Bart'+str(d.get('Bart'))

'''
set存储的是无序集合，所以我们没法通过索引来访问。访问set中的某个元素实际上就是判断一个元素是否在set中。使用in操作符判断。注：完全匹配，区分大小写。
set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
set存储的元素也是没有顺序的。
'''
s=set(['A','B','C'])
print s,len(s)
if 'A' in s:
	print 'OK'
else:
	print 'error'
s.add('D')
s.remove('A')
for num in s:
	print num

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
	print x[0]+':',x[1]

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for x in L:
	if x in s:
		s.remove(x)
	else:
		s.add(x)
print s
