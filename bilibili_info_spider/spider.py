import time
import json
import logging
import requests
import mysql.connector
from multiprocessing import Pool
from utiltools.utils import setheaders, setproxy, setlogger


info_url = 'https://space.bilibili.com/ajax/member/GetInfo'
mid = [i for i in range(2338040, 2339030)]

s = requests.Session()


def getsource(mid):
    payload = {
        'mid': mid,
        '_': int(time.time() * 1000)
    }

    s.proxies = setproxy()
    s.headers = setheaders()
    data = {}
    flag = {}

    try:
        result = s.post(info_url, data=payload).json()
        flag = result['status']
        data = result['data']
    except json.decoder.JSONDecodeError as err:
        print(json.dumps(result))
        logging.error("JSONDecodeError errors have done {}".format(err))
    except requests.exceptions.ProxyError as e:
        logging.error("ProxyError have done {}".format(e))
    finally:
        result = None

    if len(data) is 0:
        return

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
    fans = None
    friend = None
    attention = None
    sign = data['sign']
    attentions = None
    level = data['level_info']['current_level']
    exp = data['level_info']['current_exp']
    regtime_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(regtime))

    if flag is True:
        print('Succeed->%s' % (mid))
        logging.info('Succeed: ' + mid)
    else:
        logging.info('Failed: ' + mid)

    try:
        cnx = mysql.connector.connect(user='python', password='python', database='testDB')
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
        # time.sleep(30)
        result = p.map(getsource, mid)
        p.close()
        p.join()
