# 爬虫|rulopen

import urllib.request

response=urllib.request.urlopen('http://www.baidu.com')
html=response.read()
html=html.decode('utf-8')

print(html)