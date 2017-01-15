# 字典|fromkeys

# 注意使用fromkeys关键字并不会修改字典本身

dict1={}
print(dict1)

dict1=dict1.fromkeys((1,2,3))
print(dict1)

dict1=dict1.fromkeys((1,2,3),'Hi')
print(dict1)

dict1=dict1.fromkeys((1,2,3),'Hello world')
print(dict1)
