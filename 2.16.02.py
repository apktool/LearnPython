# 配置文件操作|configparser

import configparser
config = configparser.ConfigParser()

# 创建example.ini文件
config['DEFAULT'] = {'ServerAliveInterval': '45',
        'Compression': 'yes',
        'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)


temp=config.sections()
print(temp)

temp=config.options('topsecret.server.com')
print(temp)

topsecret = config['topsecret.server.com']

temp=topsecret.get('port')
print(temp)

temp=topsecret.get('Cipher','123')
print(temp)

'''
[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9
forwardx11 = yes

[bitbucket.org]
user = hg

[topsecret.server.com]
port = 50022
forwardx11 = no
'''
