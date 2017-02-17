# 简单爬虫|爬取jiandan.net图片|使用代理

import urllib.request
import re
import os

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

def get_html(url):
	proxy_handler=urllib.request.ProxyHandler({'http': '58.222.254.11:3128'});
	proxy_auth_handler=urllib.request.ProxyBasicAuthHandler()
	opener=urllib.request.build_opener(proxy_handler, proxy_auth_handler);
	opener.addheaders=[headers]

	req=opener.open(url)
	html=req.read()
	return html

def find_img(html): 
    # p=re.compile(r'https?:\/\/[a-zA-Z0-9\.\/]*\.html')
    p=re.compile(r'\/\/[a-zA-Z0-9\.\/]*\.jpg')
    addr=p.findall(html)
    addr=['http:'+each for each in addr]
    addr=list(set(addr))
    return addr

def download_img(url):
    for each in addr:
        html=get_html(each)
        with open(each[50:],'wb') as f:
            f.write(html)

if __name__=='__main__':
	dirname='example'
	try:
		os.mkdir(dirname)
	except FileExistsError as error:
		print(error)
	os.chdir(dirname)
	url='http://jandan.net/ooxx'

	html=get_html(url).decode('utf-8')
	addr=find_img(html)
	download_img(addr)
