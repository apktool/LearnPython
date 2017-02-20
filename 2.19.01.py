# 模拟登陆知乎

import urllib.request
import http.cookiejar
import time
import json
import re
import os
import pdb

url='https://www.zhihu.com'
headers={
	'Connection':'Keep-Alive',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

basicdata={
	'email':'example@domain.com',
	'password':'xxxxxxx'
}

def get_opener():
	proxy_handler=urllib.request.ProxyHandler({'121.232.147.73':'9000'})
	proxy_auth_handler=urllib.request.ProxyBasicAuthHandler()

	cookie=http.cookiejar.CookieJar()
	cookiepro=urllib.request.HTTPCookieProcessor(cookie)

	opener=urllib.request.build_opener(proxy_handler, proxy_auth_handler,cookiepro)

	header=[]
	for key,value in headers.items():
			elements=(key,value)
			header.append(elements)

	opener.addheaders=header
	return opener


def get_xsrf(html):
	p=re.compile('name="_xsrf" value="(.*)"',flags=0)
	xsfr = p.findall(html)
	return xsfr[0]

def get_html(url,opener,postdata=None):
	try:
		if postdata == None:
			req=opener.open(url)
		else:
			req=opener.open(url,postdata)
	except urllib.error.HTTPError as errhttp:
		print('HTTP error code %s -> %s'%(errhttp.code,errhttp.reason))
	except urllib.error.URLError as errurl:
		print('URL error reason %s'%(errurl.reason))

	return req

# 获取验证码
def get_captcha(opener):
	t=str(int(time.time()*1000))
	captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
	req=get_html(captcha_url,opener)
	captcha_data=req.read()

	with open('captcha.gif', 'wb') as f:
			f.write(captcha_data)
			f.close()
	captcha = input('Please input the captcha: ')
	return captcha

def get_profile(url,postdata):
	profile={}

	req=get_html(url,opener,postdata)

	html=req.read().decode('utf-8')
	p=re.compile(r'<span class="name">(.*?)</span>')
	data=p.findall(html)

	profile['name']=data[0]
	p=re.compile(r'<input autocomplete="off" class="zg-form-text-input" name="url_token" id="url_token" value="(.*?)" required>')
	data=p.findall(html)
	profile['domainname']=data[0]

	return profile


if __name__=='__main__':
	opener=get_opener()
	req=get_html(url,opener)
	mainhtml=req.read().decode('utf-8')
	xsfr=get_xsrf(mainhtml)

	urllogin=url+'/login/email'
	req=get_html(urllogin,opener)

	basicdata['_xsrf']=xsfr

	postdata=urllib.parse.urlencode(basicdata).encode('utf-8')
	req=get_html(urllogin,opener,postdata)

	data=req.read()
	js=json.loads(data)
	rcode=js['r']
	msg=js['msg']
	print(msg)

	if rcode == 0:
		profile={}
		urlprofile='https://www.zhihu.com/settings/profile'
		profile=get_profile(urlprofile,None)

		for key,value in profile.items():
			print(key+' : '+value)
	else:
		errcode=js['errcode']
		while errcode==1991829:
			captcha=get_captcha()
			basicdata['captcha']=captcha
			postdata=urllib.parse.urlencode(basicdata).encode('utf-8')
			req=get_html(urllogin,opener,postdata)
			data=req.read()
			js=json.loads(data)
			errcode=js['errcode']
