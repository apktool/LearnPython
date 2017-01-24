# 解析xml文件

from xml.dom.minidom import parse
import xml.dom.minidom

domTree=xml.dom.minidom.parse('catalog.xml')
collection=domTree.documentElement
if collection.hasAttribute('shelf'):
    print('Root element:%s'%collection.getAttribute('shelf'))


movies=collection.getElementsByTagName('movie')
#print(movies)

for movie in movies:
    if movie.hasAttribute('title'):
        print('Title:%s'%(movie.getAttribute('title')))
    types=movie.getElementsByTagName('type')[0]
    print('->| Type:%s'%(types.childNodes[0].data))
    formats=movie.getElementsByTagName('format')[0]
    print('->| Format:%s'%(types.childNodes[0].data))

