# 模拟登陆知乎|验证码问题仍未被解决

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
    proxy_handler=urllib.request.ProxyHandler({'121.232.146.118':'9000'})
    proxy_auth_handler=urllib.request.ProxyBasicAuthHandler()

    cj=http.cookiejar.CookieJar()
    pro=urllib.request.HTTPCookieProcessor(cj)

    opener=urllib.request.build_opener(proxy_handler, proxy_auth_handler,pro)

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

def get_html(url,postdata=None):
    try:
        opener=get_opener()
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
def get_captcha():
    t=str(int(time.time()*1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    print(captcha_url)
    req=get_html(captcha_url)
    captcha_data=req.read()
    
    with open('captcha.gif', 'wb') as f:
            f.write(captcha_data)
            f.close()
    captcha = input('Please input the captcha: ')
    return captcha

def get_profile(url,postdata):
    profile={}

    req=get_html(url,postdata)
    html=req.read().decode('utf-8')
    p=re.compile(r'<span class="name">(.*?)</span>')
    data=p.findall(html)

    profile['name']=data[0]
    p=re.compile(r'<input autocomplete="off" class="zg-form-text-input" name="url_token" id="url_token" value="(.*?)" required>')
    data=p.findall(html)
    profile['domainname']=data[0]

    return profile


if __name__=='__main__':
    req=get_html(url)
    mainhtml=req.read().decode('utf-8')
    xsfr=get_xsrf(mainhtml)
    
    url+='/login/email'
    print('-> '+url+' | '+xsfr)
    req=get_html(url)

    basicdata['_xsrf']=xsfr

    postdata=urllib.parse.urlencode(basicdata).encode('utf-8')
    print(postdata)
    req=get_html(url,postdata)
    print('------------------')
    print(req)
    print('------------------')

    
    data=req.read()
    js=json.loads(data)
    rcode=js['r']
    msg=js['msg']
    print(msg)

    if rcode == 0:
        profile={}
        url='https://www.zhihu.com/settings/profile'
        profile=get_profile(url,postdata)

        for key,value in profile.items():
            print(key+' : '+value)
    else:
        errcode=js['errcode']
        while errcode==1991829:
            captcha=get_captcha()
            basicdata['captcha']=captcha
            postdata=urllib.parse.urlencode(basicdata).encode('utf-8')
            req=get_html(url,postdata)
            data=req.read()
            js=json.loads(data)
            errcode=js['errcode']
