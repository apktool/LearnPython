import logging
import random


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q = 0.8',
    'Connection': 'keep-alive',
    'Host': 'space.bilibili.com',
    'Origin': 'https://space.bilibili.com',
    'Referer': '',
    'User-Agent': ''
}

proxies = {
    'http': 'http://122.193.14.103:81',
    'https': 'https://119.23.63.152:8118'
}


def setheaders():
    agent = setagent()
    headers['User-Agent'] = random.choice(agent)
    headers['Referer'] = 'http://space.bilibili.com/' + str(random.randint(9000, 10000)) + '/'
    return headers


def setproxy():
    proxies_pool = []
    with open('proxies/ipproxy.txt', 'r') as f:
        for line in f:
            proxies_pool.append(line.rstrip())
    item = proxies_pool[random.randint(0, len(proxies_pool)-1)]
    key = item.split()[0].split(':')[0]
    value = item.split()[1]
    proxies[key] = value
    return proxies


def setagent():
    uas = []
    with open('proxies/useragent.txt', 'r') as f:
        for line in f.readlines():
            if line is not None:
                uas.append(line.strip()[1:-1 - 1])
    random.shuffle(uas)
    return uas


def setlogger():
    logging.getLogger('').setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    files = logging.FileHandler('log/example.log')
    files.setLevel(logging.DEBUG)
    files.setFormatter(formatter)
    logging.getLogger('').addHandler(files)
