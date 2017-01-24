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

'''catalog.xml
<collection shelf="New Arrivals">
<movie title="Enemy Behind">
    <type>War, Thriller</type>
    <format>DVD</format>
    <year>2003</year>
    <rating>PG</rating>
    <stars>10</stars>
    <description>Talk about a US-Japan war</description>
</movie>
<movie title="Transformers">
    <type>Anime, Science Fiction</type>
    <format>DVD</format>
    <year>1989</year>
    <rating>R</rating>
    <stars>8</stars>
    <description>A schientific fiction</description>
</movie>
<movie title="Trigun">
    <type>Anime, Action</type>
    <format>DVD</format>
    <episodes>4</episodes>
    <rating>PG</rating>
    <stars>10</stars>
    <description>Vash the Stampede!</description>
</movie>
<movie title="Ishtar">
    <type>Comedy</type>
    <format>VHS</format>
    <rating>PG</rating>
    <stars>2</stars>
    <description>Viewable boredom</description>
</movie>
</collection>
'''
