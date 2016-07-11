# coding=utf-8
# author: shuqing.zhou

import datetime
from multiprocessing.dummy import Pool as ThreadPool

import requests
from bs4 import BeautifulSoup

from eggs.utils import mail

receivers = ["xutao.ding@chinascopefinancial.com"]


class Tjsoc(object):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=8me0jtfsj2ampas6cnq2d14433',
        'Host': 'www.tjsoc.com',
        'Pragma': 'no-cache',
        "Referer": 'http":"//www.tjsoc.com/Article/lists/category/78/p/2.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.103 Safari/537.36'
    }

    def fetch(self, url):
        for i in range(0, 5):
            try:
                return requests.get(url, headers=self.headers, timeout=30)
            except Exception as e:
                print i, e.message

    def __get_page(self):
        url = "http://www.tjsoc.com/Article/lists/category/78/p/1.html"
        try:
            r = self.fetch(url)
            soup = BeautifulSoup(r.content, "lxml")
            return int(soup.select_one(".end").text.strip())
        except Exception as e:
            print e.message

        return 0

    def parse(self, url):
        ret = []
        r = self.fetch(url)
        soup = BeautifulSoup(r.content, "lxml")
        for item in soup.select(".zmwh_b ul li"):
            data = ";".join([span.text.strip() for span in item.select("span")])
            ret.append(data)
        return ret

    def main(self):
        page = self.__get_page()
        urls = ["http://www.tjsoc.com/Article/lists/category/78/p/%s.html" % i for i in range(1, page + 1)]
        pool = ThreadPool(12)
        result = pool.map(self.parse, urls)
        pool.close()
        pool.join()

        mail.Sender(receivers=receivers).send_email(
            subject="%s 天津股权交易所股权挂牌交易行情" % str(datetime.date.today()),
            body="%s 天津股权交易所股权挂牌交易行情" % str(datetime.date.today()),
            attaches=[{
                'attach_text': u"股权名称;股权代码;收盘价;成交量\n" + '\n'.join([_ for r in result for _ in r]),
                'attach_name': '天津股权信息.txt'
            }])


if __name__ == '__main__':
    import time

    start = time.time()
    Tjsoc().main()
    print('Need time: {} seconds.'.format(time.time() - start))


