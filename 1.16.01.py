# 列表生成式

temp=list(range(1,11))
print(temp)

#y=x*x

temp=[x*x for x in range(1,11)]
print(temp)

temp=[x*x for x in range(1,11) if x%2 ==0]
print(temp)

# 生成'ABC'和'XYZ'的每个字母的组合

temp=[m+n for m in 'ABC' for n in 'XYZ']
print(temp)
