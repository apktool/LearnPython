# 爬虫|使用有道字典实现翻译

import urllib.request
import urllib.parse
import json

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

content='I love you'

data={
'type':'AUTO',
'i':content,
'doctype':'json',
'xmlVersion':'1.8',
'keyfrom':'fanyi.web',
'ue':'UTF-8',
'action':'FY_BY_CLICKBUTTON',
'typoResult':'true'
}

data=urllib.parse.urlencode(data).encode('utf-8')
req=urllib.request.Request(url,data)

req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')

response=urllib.request.urlopen(url,data)

html=response.read().decode('utf-8')

target=json.loads(html)
result=target['translateResult'][0][0]['tgt']
print(result)
