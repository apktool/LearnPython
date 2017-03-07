# 爬取bilibili基本用户信息|使用MySql

import time
import logging
import requests
import mysql.connector
from multiprocessing import Pool


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q = 0.8',
    'Connection': 'keep-alive',
    'Host': 'space.bilibili.com',
    'Origin': 'https://space.bilibili.com',
    'Referer': 'http://space.bilibili.com/2337891/',  # 这句很重要
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

proxies = {
    'http://121.232.147.124:9000': 'https://113.222.81.103:9797'
}

info_url = 'https://space.bilibili.com/ajax/member/GetInfo'
mid = [i for i in range(2338000, 2338030)]

s = requests.Session()
s.headers = headers
s.proxies = proxies


def setlogger():
    logging.getLogger('').setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    files = logging.FileHandler('example.log')
    files.setLevel(logging.DEBUG)
    files.setFormatter(formatter)
    logging.getLogger('').addHandler(files)


def getsource(mid):
    payload = {
        'mid': mid,
        '_': int(time.time() * 1000)
    }
    result = s.post(info_url, data=payload).json()

    flag = result['status']
    data = result['data']

    mid = data['mid']
    name = data['name']
    sex = data['sex']
    face = data['face']
    coins = data['coins']
    regtime = data['regtime']
    spacesta = data['spacesta']
    birthday = data['birthday']
    place = data['place']
    description = data['description']
    article = data['article']
    fans = data['fans']
    friend = data['friend']
    attention = data['attention']
    sign = data['sign']
    attentions = data['attentions']
    level = data['level_info']['current_level']
    exp = data['level_info']['current_exp']
    regtime_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(regtime))

    if flag is True:
        print('Succeed->%s' % (mid))
        logging.info('Succeed: ' + mid)
    else:
        logging.info('Failed: ' + mid)

    try:
        cnx = mysql.connector.connect(user='python', password='Python@2017', database='testDB')
    except mysql.connector.Error as err:
        print("Connetion errors have done {}".format(err))
    finally:
        cursor = cnx.cursor()

    cursor.execute('INSERT INTO bilibili_user_info VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', [mid, mid, name, sex, face, coins, regtime_format, spacesta, birthday, place, description, article, fans, friend, attention, sign, str(attentions), level, exp])

    cnx.commit()


if __name__ == '__main__':
    setlogger()
    p = Pool(5)
    try:
        result = p.map(getsource, mid)
    except Exception as error:
        print('Error connection')
        time.time(3000)
        result = p.map(getsource, mid)
    p.close()
    p.join()

'''
创建数据库
CREATE DATABASE testDB;
创建表格
CREATE TABLE `bilibili_user_info` (
`id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
`mid` VARCHAR(11) DEFAULT NULL,
`name` VARCHAR(45) DEFAULT NULL,
`sex` VARCHAR(11) DEFAULT NULL,
`face` VARCHAR(200) DEFAULT NULL,
`coins` INT(11) DEFAULT NULL,
`regtime` VARCHAR(45) DEFAULT NULL,
`spacesta` INT(11) DEFAULT NULL,
`birthday` VARCHAR(45) DEFAULT NULL,
`place` VARCHAR(45) DEFAULT NULL,
`description` VARCHAR(45) DEFAULT NULL,
`article` INT(11) DEFAULT NULL,
`fans` INT(11) DEFAULT NULL,
`friend` INT(11) DEFAULT NULL,
`attention` INT(11) DEFAULT NULL,
`sign` VARCHAR(300) DEFAULT NULL,
`attentions` TEXT,
`level` INT(11) DEFAULT NULL,
`exp` INT(11) DEFAULT NULL,
PRIMARY KEY (`id`)
)ENGINE=MYISAM DEFAULT CHARSET=UTF8;
'''
