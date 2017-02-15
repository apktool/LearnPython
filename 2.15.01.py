# 简单爬虫|爬取jiandan.net图片|正则表达式

import urllib.request
import re
import os

def get_html(url):
    req=urllib.request.urlopen(url)
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
    os.mkdir('temp')
    os.chdir('temp')
    url='http://jandan.net/ooxx'
    html=get_html(url).decode('utf-8')
    addr=find_img(html)
    download_img(addr)
