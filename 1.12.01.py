#--coding:utf-8---

#元组

tuple1=(1,2,3,4,5,6,7,8)
print(tuple1)

tuple2=(1)
print(tuple2)

tuple3=(1,)
print(tuple3)

tuple4=1
print(tuple4)

tuple5=1,
print(tuple5)

'''
应该注意tuple2和tuple3的区别：tuple2创建的是一个整数，tuple3创建的是一个元祖
tuple4创建的是一个整数，tuple5创建的是一个元组
'''

a=8*(8)
print(a)

a=8*(8,)
print(a)

'''
第一次打印出的a是64
第二次打印出的a是(8, 8, 8, 8, 8, 8, 8, 8)
'''

temp=('a','b','d')
print(temp);

temp=temp[:2]+('c',)+temp[2:]
print(temp);

'''
向已有元组中添加元素
'''
