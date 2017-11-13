import json
import uuid
import logging
import requests
import mysql.connector
from multiprocessing import Pool
from utiltools.utils import setheaders, setproxy, setlogger


info_url = 'https://space.bilibili.com/ajax/Bangumi/GetList?mid=%d&page=%d'
mid = [i for i in range(6730000, 6740000)]

s = requests.Session()


def getdata(mid, page):
    flag = {}
    data = {}

    try:
        url = info_url % (mid, page)
        result = s.get(url).json()
        flag = result['status']
        data = result['data']
    except json.decoder.JSONDecodeError as err:
        print(json.dumps(result))
        logging.error("JSONDecodeError errors have done {}".format(err))
    except requests.exceptions.ProxyError as e:
        logging.error("ProxyError have done {}".format(e))
    finally:
        result = None

    if flag is True:
        print('Succeed->%d' % mid)
        logging.info('Succeed: ' + str(mid))
    else:
        logging.info('Failed: ' + str(mid))
    return data


def executesql(mid, results):
    for item in results:
        season_id = item['season_id']
        share_url = item['share_url']
        title = item['title']
        is_finish = item['is_finish']
        favorites = item['favorites']
        newest_ep_index = item['newest_ep_index']
        last_ep_index = item['last_ep_index']
        total_count = item['total_count']
        cover = item['cover']
        evaluate = item['evaluate']
        brief = item['brief']

        try:
            cnx = mysql.connector.connect(user='python', password='python', database='testDB')
        except mysql.connector.Error as err:
            print("Connetion errors have done {}".format(err))
        finally:
            cursor = cnx.cursor()

        cursor.execute('INSERT INTO bilibili_anime_info VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', [str(uuid.uuid4()), mid, season_id, title, brief, favorites, total_count, is_finish, last_ep_index, newest_ep_index, cover, share_url, evaluate])

        cnx.commit()


def getsource(mid):
    s.proxies = setproxy()
    s.headers = setheaders()

    data = getdata(mid, 1)

    if len(data) is 0 or isinstance(data, str):
        return

    count = data['count']
    pages = data['pages']
    results = data['result']
    executesql(mid, results)

    for page in range(2, pages + 1):
        data = getdata(mid, page)
        results = data['result']
        executesql(mid, results)


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
