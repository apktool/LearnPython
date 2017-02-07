# 迭代器

string='hello world'

it=iter(string)

temp=next(it)
print(temp)

print(next(it))
print(next(it))

#---------------------
print('--->')

string='hello world'
it=iter(string)

while True:
	try:
		each=next(it)
	except StopIteration:
		break
	print(each)
