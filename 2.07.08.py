# 定制容器

class Countlist(object):
	def __init__(self,*args):
		self.values=[x for x in args]
		self.count={}.fromkeys(range(len(self.values)),0)
	
	def __len__(self):
		return len(self.values)

	def __getitem__(self,key):
		self.count[key]+=1
		return self.values[key]

c1=Countlist(1,3,5,7,9)
c2=Countlist(2,4,6,8,10)

print(c1[1])
print('c1[1]+c2[2]=%d '%(c1[1]+c2[1]))

print(c1.count)

'''
定制的容器要求不可变，只需要定义__len__()和__getitem__()方法
定制的容器要求可变，除了__len__()和__getitem__()方法之外，还需要定义__setitem__()和__delitem__()方法
'''
