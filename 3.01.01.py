# 爬取bilibili基本用户信息

import requests
import time
import pdb
from multiprocessing import Pool

headers={
	'Accept':'application/json, text/plain, */*',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Connection':'keep-alive',
	'Host':'space.bilibili.com',
	'Origin':'https://space.bilibili.com',
	'Referer':'http://space.bilibili.com/2337891/',#这句很重要
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

proxies={
	'http://121.232.147.124:9000':'https://113.222.81.103:9797'
}

info_url='https://space.bilibili.com/ajax/member/GetInfo'
mid=[i for i in range(2337880,2337900)]

s=requests.Session()
s.headers=headers
s.proxies=proxies

def getsource(mid):
	payload={
		'mid':mid,
		'_':int(time.time()*1000)
	}
	result=s.post(info_url,data=payload).json()
	flag=result['status']
	data=result['data']
	print('------')
	print(data['mid'])
	print(data['name'])
	print(data['sex'])
	print(data['attention'])
	print(data['fans'])
	print(data['friend'])

if __name__=='__main__':
	p=Pool(5)
	try:
		result=p.map(getsource,mid)
	except Exception as error:
		print('Error connection')
		time.time(3000)
		result=p.map(getsource,urls)
	p.close()
	p.join()
