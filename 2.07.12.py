# 推导式

# 列表推导式
a=[i for i in range(10) if not i%2 and i%3]
print(a)

# 字典推导式
b={i:i%2==0 for i in range(10)}
print(b)

# 集合推导式
c={i for i in [1,1,2,3,4,5,5,6,7]}
print(c)

# 生成器推导式
d=(i for i in range(10))
print(d)
print(next(d))
print(next(d))

temp=sum(i for i in range(100) if i%2)
print(temp)
