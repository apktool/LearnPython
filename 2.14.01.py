# 简单爬虫|爬取jiandan.net图片

import urllib.request
import os

def get_html(url):
	req=urllib.request.Request(url)
	#req.add_header('User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
	response=urllib.request.urlopen(req)
	html=response.read()
	return html

def find_img(html):
	img_list=[]
	
	a=html.find('<img src=')
	while a!=-1:
		b=html.find('.jpg',a,a+128)
		if b != -1:
			img_list.append('http:'+html[a+10:b+4])
		else:
			b=a+10
		a=html.find('<img src=',b)

	return img_list

def download_img(url):
	html=get_html(url).decode('utf-8')
	img_list=find_img(html)

	for each in img_list:
		img_html=get_html(each)
		name=each[28:]
		with open(name,'wb') as f:
			f.write(img_html)

if __name__=='__main__':
	os.mkdir('temp')
	os.chdir('temp')

	url='http://jandan.net/ooxx'
	download_img(url)
