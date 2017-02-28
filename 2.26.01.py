# 模拟登陆知乎|使用requests库

import requests
import http.cookiejar
import re
import time
import json

url='https://www.zhihu.com'
headers={
    'Connection':'Keep-Alive',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

proxies={
	'http://119.98.142.44:8998':'https://112.95.20.82:6666'
}

personaldata={
    'email':'example@domain.com',
    'password':'xxxxxxxx'
}

session=requests.Session()
session.proxies=proxies
session.cookies=http.cookiejar.LWPCookieJar(filename='cookie')
try:
	session.cookies.load(ignore_discard=True)
except:
	print('error Cookie')

def get_xsrf():
	indexurl=url
	indexpage=session.get(indexurl,headers=headers)
	html=indexpage.text
	p=re.compile(r'name="_xsrf" value="(.*?)"')
	_xsrf=p.findall(html)
	return _xsrf[0]

def get_captcha():
	t=str(int(time.time()*1000))
	captcha_url=url+'/captcha.gif?r='+t+"&type=login"
	r = session.get(captcha_url, headers=headers)
	with open('captcha.gif','wb') as f:
		f.write(r.content)
		f.close()
	captcha=input("please input the captcha\n>")
	return captcha

def login(account,passwd):
	postdata={
		'_xsrf':get_xsrf(),
		'email':account,
		'password':passwd,
		'remember_me':'true',
	}

	posturl=url+'/login/email'

	try:
		loginpage=session.post(posturl,data=postdata,headers=headers)
		logincode=loginpage.text
		print('loginpage.status:%s'%(loginpage.status))
		print('logincode:%s'%(logincode))
	except:
		postdata['captcha']=get_captcha()
		loginpage=session.post(posturl, data=postdata, headers=headers)
		logincode=eval(loginpage.text)
		print(logincode['msg'])

	session.cookies.save()

def islogin():
	personurl=url+'/settings/profile'
	logincode=session.get(personurl,headers=headers,allow_redirects=False).status_code
	print('logincode:%s'%logincode)
	if int(logincode) == 200:
		return True
	else:
		return False

if __name__=='__main__':
	login(personaldata['email'],personaldata['password'])
	if islogin()==True:
		print('Success loggin')
	else:
		print('islogin:%s'%(islogin()))
		print('Fail loggin')
