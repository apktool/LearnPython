# nonlocal

def Fun1():
	x=5
	def Fun2():
		nonlocal x
		x*=x
		return x
	return Fun2()

temp=Fun1()
print(temp)
