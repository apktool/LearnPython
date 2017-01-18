# 类|self

class Ball:
	def setName(self,name):
		self.name=name;
	def kick(self):
		print('%s' % self.name)

a=Ball()
a.setName('haha')
a.kick()

b=Ball()
b.setName('ahah')
b.kick()
