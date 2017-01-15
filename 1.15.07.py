# 访问字典，修改字典

dict1={}
dict1=dict1.fromkeys(range(5),'Hit')
print(dict1)

# 访问key

for i in dict1.keys():
	print(i)

# 访问value

for i in dict1.values():
	print(i)

# 访问item

for i in dict1.items():
	print(i)

# print(dict1[5]) # 因为并不存在5号元素，故会报错
print(dict1.get(5,'No')) # 使用get方法可以避免生硬的报错

dict1=dict1.clear() # 清空字典元素

'''
example:
	dict1={1:1,2:2}
	dict2=dict1

	使用dict1={}可以清空dict1元素，但dict2中的元素仍然保留
	使用dict1.clear{}可以同时清空dict1和dict2元素

使用id可以查看地址，比如id(dict1)
'''
print("---------------------------------")

dict2={}
dict2=dict2.fromkeys(range(5),'Hit')
print(dict2)

print(dict2)
temp=dict2.pop(2)
print(temp)
print(dict2)

temp=dict2.popitem()
print(temp)
print(dict2)

dict2.setdefault('Small')
print(dict2)

dict2.setdefault('Big',9)
print(dict2)

temp={'Middle':5}
dict2.update(temp)
print(dict2)
