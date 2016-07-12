# -*-coding:utf-8 -*-
'''
切片：
L[0:3]表示对列表L的前三个元素进行一次索引
L[3:3]表示从第3号元素开始，索引其后的三个元素
L[1:50:3]表示从1号元素索引到地50号元素，每个元素的间隔是3
'''
L=range(0,100)
print L[0:10]
print L[2::3]
print L[4:50:5]
print L[-10:-1]
print L[5::5][-10:]#最后10个5的倍数

def firstCharUpper(s):
	return s[:1].upper()+s[1:]

print firstCharUpper('hello');

#打印100以内，7的倍数
for x in range(7,101,7):
	print x

#打印100以内，7的倍数
for x in range(1,101)[6:100:7]:
	print x;

'''
集合是指包含一组元素的数据结构，我们已经介绍的包括：
1. 有序集合：list，tuple，str和unicode；
2. 无序集合：set
3. 无序集合并且具有 key-value 对：dict
'''

#python中，迭代永远是取出元素本身，而非元素的索引；
#如果想要取出索引号，则需要使用enumerate
L=['Adam','Lisa','Bart','Paul']
for index,name in enumerate(L):
	print index+1,'-',name
