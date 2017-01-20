# 计时器的简单实现

import time as t

class MyTimer():
	def __init__(self):
		self.unit=['year','month','days','hour','minute','second']
		self.prompt='未开始计时'
		self.lasted=[]
		self.begin=0
		self.end=0

	def __str__(self):
		return self.prompt

	__repr__=__str__

	def __and__(self, other):
		prompt='toal '
		result=[]
		for index in range(6):
			result.append(self.lasted[index]+other.lasted[index])
			if result[index]:
				prompt+=(str(result[index])+self.unit[index])
		return prompt

	def start(self):
		self.begin=t.localtime()
		print('start time...')

	def stop(self):
		self.end=t.localtime()
		self._calc()
		print('finish time...')

	def _calc(self):
		self.lasted=[]
		self.prompt='The toal time you ran: '
		for index in range(6):
			self.lasted.append(self.end[index]-self.begin[index])
			if self.lasted[index]:
				self.prompt+=(str(self.lasted[index])+' '+self.unit[index])
		self.begin=0
		self.end=0

t1=MyTimer()
t1.start()
x=[i for i in range(1,10000000) if i%2!=0]
t1.stop()
print(t1)

t2=MyTimer()
t2.start()
x=[i for i in range(1,10000000) if i%2!=0]
t2.stop()
print(t2)

# print(t1+t2)
