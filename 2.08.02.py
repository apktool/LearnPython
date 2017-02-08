
import urllib.request

response=urllib.request.urlopen('http://placekitten.com/500/600')
cat_img=response.read()

temp=response.geturl()
print(temp)

print('-----------------')

temp=response.info()
print(temp)

print('-----------------')

temp=response.getcode()
print(temp)

with open('cat_500_600.jpg','wb') as f:
	f.write(cat_img)

'''
response=urllib.request.urlopen('http://placekitten.com/500/600')
等价于
req=urllib.request.Request('http://placekitten.com/500/600')
response=urllib.request.urlopen(req)
'''
