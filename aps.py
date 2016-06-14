# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import os
import sys
import hashlib
import logging
from os.path import dirname, abspath
from datetime import date, timedelta, datetime

import requests
import simplejson
from pymongo import MongoClient
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)


def create_sqlite():
    sqlite_path = dirname(abspath(__file__))
    for sql_path in os.listdir(sqlite_path):
        if sql_path.endswith('.db'):
            os.remove(os.path.join(sqlite_path, sql_path))

create_sqlite()

jobstores = {
    # 'default': MemoryJobStore()
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.db')
}

# using ThreadPoolExecutor as default other than ProcessPoolExecutor(not work) to executors
executors = {
    'default': ThreadPoolExecutor(2),
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

app = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)


def md5(value):
    if not isinstance(value, basestring):
        raise ValueError('md5 must string!')
    m = hashlib.md5()
    try:
        m.update(value)
    except UnicodeEncodeError:
        m.update(value.encode('u8'))
    return m.hexdigest()


def get_date_range(start, end):
    """
    calculate date range
    :param start: string, yyyymmdd, start date
    :param end: string, yyyymmdd, end date
    :return: list, date string range list
    """
    date_range = []
    split_ymd = (lambda _d: (int(_d[:4]), int(_d[4:6]), int(_d[6:8])))
    date_start = date(*split_ymd(start))
    date_end = date(*split_ymd(end))

    while date_start <= date_end:
        date_range.append(str(date_start).replace('-', ''))
        date_start = timedelta(days=1) + date_start
    return date_range


# @app.scheduled_job(trigger='cron', hour='0', minute='0', second='0', misfire_grace_time=5)
def insert2mongo(query_date=None):
    """
    This task request `http://54.223.52.50:8005/api/news/amazon/stat/data.json`, query string: date=00000000,
    then insert `192.168.100.15`

    :param query_date: string, request query string, default is None,
    :return:
    """
    host, port = '192.168.100.15', 27017
    # host, port = '192.168.100.20', 27017
    today = str(date.today() - timedelta(days=1)).replace('-', '')
    request = 'http://54.223.52.50:8005/api/news/amazon/stat/data.json?date=%s'

    if query_date is None:
        query_string = today
    else:
        query_string = query_date

    db = MongoClient(host, port)
    collection = db.log.news_stat
    overall_uid = {docs['uid'] for docs in collection.find({}, {'uid': 1})}

    try:
        req = requests.get(url=request % query_string, timeout=30)
        to_python = simplejson.loads(req.content)

        for site_key, _docs in to_python.iteritems():
            uid = md5(site_key + query_string)
            _docs.update(site=site_key, uid=uid, crt=datetime.now())

            if uid not in overall_uid:
                collection.insert(_docs)
            else:
                if query_date == today:
                    collection.remove({'uid': uid})
                    collection.insert(_docs)
    except Exception as e:
        logging.info('Insert mongo error: type <{}>, msg <{}>'.format(e.__class__, e))
    else:
        logging.info('\t<{}> query is success from amazon.'.format(query_date))
    db.close()


def count_with_corpus(query_date=None):
    host, port = '192.168.100.15', 27017
    today = str(date.today() - timedelta(days=1))
    client = MongoClient(host, port)
    collection = client.log.corpus_stat
    query_string = today if query_date is None else query_date
    overall_uid = {docs['uid'] for docs in collection.find({}, {'uid': 1})}

    all_corpus = {'weixin': u'微信文章', 'zhihu': u'知乎股票评论', 'baidu': u'百度新闻',
                  'xuwqiu': u'雪球股票评论', 'guba': u'东方财富股吧股票评论', 'jobs': u'拉钩', 'comp': u'公司信息', }
    corpus_base = 'http://192.168.250.207:7900/api/corpus/{corpus}/data.json?date={date}'

    for corpus in all_corpus:
        try:
            uid = md5(corpus + query_string)
            resp = requests.get(corpus_base.format(corpus=corpus, date=query_string), timeout=30)
            to_python = simplejson.loads(resp.content)

            if uid not in overall_uid:
                key = query_string.replace('-', '')
                data = {
                    'dt': query_string,
                    'uid': uid, 'crt': datetime.now(),
                    'count': to_python[key],
                    'cat': all_corpus[corpus]
                }
                collection.insert(data)
        except Exception as e:
            logging.info('Insert mongo <{}> error: type <{}>, msg <{}>'.format(host, e.__class__, e))
        else:
            logging.info('\t<{}> query is success from <{}> .'.format(query_date, host))
    client.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        app.add_job(insert2mongo, trigger='cron', hour='0', minute='0', second='0', misfire_grace_time=5)
        app.add_job(count_with_corpus, trigger='cron', hour='0', minute='05', second='0', misfire_grace_time=5)
        app.start()
    else:
        _date_range = get_date_range(*args)
        for _query_date in _date_range:
            insert2mongo(_query_date)
