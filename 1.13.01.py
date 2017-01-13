#--coding:utf-8--

a=[]
print(a)

b="I love you"
print(b)

b=list(b)
print(b)

c=[1,3,5,7,9,8,6,4,2,0]

print(len(c))
print(max(c))
print(min(c))

# list里面可以存放不同类型的元素

d=[1,2,'a',1.5,(3,4)]
print(d)

str=[4,0,3,2,1]
print(str)

# list逆序

str=list(reversed(str))
print(str)

str=list(reversed(sorted(str)))
print(str)

# enumerate

str=list(enumerate(str))
print(str)

# zip

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
str=list(zip(a,b,c))
print(a)
print(b)
print(c)
print(str)
