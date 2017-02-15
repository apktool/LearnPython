# 正则表达式|search

import re

# search()

result=re.search(r' (\w+) (\w+)','I love you')
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.start())
print(result.end())
print(result.span())

print('-------------------------')
