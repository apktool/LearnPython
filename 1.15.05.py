# 字典|创建字典
'''
键-值
'''

# 不使用字典来实现字典的功能

brand=['LiNing','Nike','Adidas']
slogan=['Anything is possible','Just do it','Impossible is nothing']
print('LiNing\'s slogan is \"',slogan[brand.index('LiNing')],'\"')

# 创建字典|使用{}

dict1={'LiNing':'Anything is possible','Nike':'Just do it','Adidas':'Impossible is nothing'}
print('LiNing\'s slogan is \"',dict1['LiNing'])
print(dict1)

# 创建字典|使用dict关键字和()

dict2=dict((('LiNing','Anything is possible'),('Nike','Just do it'),('Adidas','Impossible is nothing')))
print(dict2)
