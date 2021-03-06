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
    'default': ThreadPoolExecutor(10),
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
        req = requests.get(url=request % query_string, timeout=60)
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
        logging.info('\t<{}> query is success from amazon.'.format(query_string))
    db.close()


def count_news_before():
    """统计新闻在抓取后且分析前各新闻的总数"""
    host, port = '192.168.100.15', 27017
    today = str(date.today() - timedelta(days=1))
    url = 'http://54.223.52.50:8005/api/news/amazon/total/data.json?date=%s'
    client = MongoClient(host, port)
    collection = client.log.news_crawled_before

    try:
        history_query = {"dt": "2016-06-25"}
        history_data = collection.find(history_query)

        if history_data.count() != 1:
            raise ValueError('历史数据 只有一条记录， 请检查条件: <%s %s %s %s>, <%s>' %
                             (host, port, 'log', 'news_crawled_before', history_query))
        else:
            history_record = history_data[0]

        req = requests.get(url % today, timeout=60)
        to_python = simplejson.loads(req.content)

        for key, value in to_python.items():
            if key != 'dt':
                to_python[key] = value + history_record[key]
        else:
            to_python['dt'] = today
        collection.insert(to_python)
    except Exception as e:
        logging.info('Error (news crawled before): type <{}>, msg <{}>'.format(e.__class__, e))
    else:
        logging.info('\t<{}> query is success from amazon(news crawled before).'.format(today))


def count_with_corpus(query_date=None):
    """
    Count comment crawled data from `eastmoney` guba, sogou weixin and so on
    :param query_date: string, format 0000-00-00
    :return:
    """
    host, port = '192.168.100.15', 27017
    today = str(date.today() - timedelta(days=1))
    client = MongoClient(host, port)
    collection = client.log.corpus_stat
    query_string = today if query_date is None else query_date
    overall_uid = {docs['uid'] for docs in collection.find({}, {'uid': 1})}

    all_corpus = {
        'weixin': u'微信文章', 'zhihu': u'知乎股票评论', 'baidu': u'百度新闻', 'xueqiu': u'雪球股票评论',
        'guba': u'东方财富股吧股票评论', 'jobs': u'拉钩', 'comp': u'公司信息',
        'patent': u'专利数据', 'bigv': u'雪球大V', 'etffund': u'ETF基金', 'innotree': u'因果树',
        'us': u'美股公告', 'hk': u'港股英文公告', 'hk_chz': u'港股中文公告', 'otc': u'新三板公告', 'report': u'研报',
        'execu': u'高管增减持', 'margin': u'融资融券 ', 'trade': u'大宗交易'
    }
    corpus_base = 'http://192.168.250.207:7900/api/corpus/{corpus}/data.json?date={date}'
    corpus_history = 'http://192.168.250.207:7900/api/corpus/{corpus}/data.json?rtype=2&date={date}'

    for corpus in all_corpus:
        try:
            uid = md5(corpus + query_string)
            # 每日各站点的评论性语料统计
            resp = requests.get(corpus_base.format(corpus=corpus, date=query_string), timeout=60)
            to_python = simplejson.loads(resp.content)

            # 各站点的评论性语料统计，在当天之前所有历史统计
            history_resp = requests.get(corpus_history.format(corpus=corpus, date=query_string), timeout=60)
            to_history = simplejson.loads(history_resp.content)

            if uid not in overall_uid:
                key = query_string.replace('-', '')
                data = {
                    'dt': query_string,
                    'uid': uid, 'crt': datetime.now(),
                    'count': to_python[key],
                    'cat': all_corpus[corpus],
                    'total_count': to_history[query_string.replace('-', '')]
                }
                collection.insert(data)
        except Exception as e:
            logging.info('Insert mongo <{}> error: type <{}>, msg <{}>'.format(host, e.__class__, e))
        else:
            logging.info('\t<{}> query is success from <{}> .'.format(query_string, host))
    client.close()


def get_count_with_news_category(query_date=None):
    """
    Count all news category from crawled news and just before analysis

    A: to every day: http://54.223.52.50:8005/api/news/amazon/origin/data.json?date=20160615
    B: to all news: http://54.223.52.50:8005/api/news/amazon/total/data.json
    C: to all news source: http://54.223.52.50:8005/api/news/amazon/source/data.json

    Note log database include `dif`, which is 0 indicate A, 1 indicate B, 2 indicate C

    :param query_date: string, format 0000-00-00
    :return:
    """
    host, port = '192.168.100.15', 27017
    today = str(date.today() - timedelta(days=1))
    client = MongoClient(host, port)
    collection = client.log.category_stat

    query_date = today.replace('-', '') if not query_date else query_date
    dt = today if not query_date else '%s-%s-%s' % (query_date[:4], query_date[4:6], query_date[6:])

    news_day_url = 'http://54.223.52.50:8005/api/news/amazon/origin/data.json?date={}'
    news_source_url = 'http://54.223.52.50:8005/api/news/amazon/source/data.json'

    try:
        # 记录当天新闻分类的总数， 且这些新闻是在分析之前
        response_news_day = requests.get(news_day_url.format(query_date), timeout=40).content
        to_python_day = simplejson.loads(response_news_day)
        to_python_day.update(dt=dt, dif=0, crt=datetime.now())
        collection.insert(to_python_day)

        # 记录所有新闻分类的来源总数
        response_news_source = requests.get(news_source_url, timeout=40).content
        to_python_source = simplejson.loads(response_news_source)
        to_python_source.update(dt=dt, dif=2, crt=datetime.now())

        query = {'dif': 2}
        if not collection.find_one(query):
            collection.insert(to_python_source)
        else:
            collection.update(query, {'$set': to_python_source})
    except Exception as e:
        logging.info('Insert mongo <{} {}> error: type <{}>, msg <{}>'.format(host, 'category_stat', e.__class__, e))
    else:
        logging.info('\t<{} {}> query is success from <{}> .'.format('category_stat', query_date, host))
    client.close()


def corpus_amazon():
    """ 统计北京亚马逊相关预料数据 """
    client = MongoClient('192.168.100.15', 27017)
    coll = client['log']['corpus_stat']
    corpus_api = 'http://54.223.52.50:8005/api/news/amazon/wencai/data.json?date={date}'

    default_date = str(date.today() - timedelta(days=1))

    try:
        r = requests.get(corpus_api.format(date=default_date), timeout=60)
        response = r.content
        to_python = simplejson.loads(response)

        to_python['uid'] = md5('wencai' + default_date)
        to_python['crt'] = datetime.now()
        to_python['cat'] = u'知识图谱_问财'
        coll.insert(to_python)
    except Exception as e:
        logging.info('corpus amazon error: typ <{}>, msg <>'.format(e.__class__, e))
    else:
        logging.info('corpus amazon insert ok!')
    client.close()

if __name__ == '__main__':
    app.add_job(insert2mongo, trigger='cron', hour='0', minute='0', second='0', misfire_grace_time=5)
    app.add_job(count_news_before, trigger='cron', hour='0', minute='2', second='0', misfire_grace_time=5)
    app.add_job(count_with_corpus, trigger='cron', hour='0', minute='5', second='0', misfire_grace_time=5)
    app.add_job(get_count_with_news_category, trigger='cron', hour='0', minute='8', second='0', misfire_grace_time=5)
    app.add_job(corpus_amazon, trigger='cron', hour='0', minute='10', second='0', misfire_grace_time=5)
    app.start()