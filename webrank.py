# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from math import log10
from os.path import dirname, abspath
from datetime import date, datetime, timedelta
from collections import defaultdict

from tld import get_tld
from pymongo import MongoClient

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor


def create_sqlite():
    sqlite_path = dirname(abspath(__file__))
    for sql_path in os.listdir(sqlite_path):
        if sql_path.endswith('.db'):
            os.remove(os.path.join(sqlite_path, sql_path))

create_sqlite()


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.db')
}

# using ThreadPoolExecutor as default other than ProcessPoolExecutor(not work) to executors
executors = {
    'default': ThreadPoolExecutor(4),
    # 'default': ProcessPoolExecutor(4),
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

app = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

SITE_NAME_MAP = {
    '163': ('网易财经', 'http://money.163.com/', 1.0),
    'cnforex': ('环球外汇', 'http://www.cnforex.com/', 0.6),
    'chineseworldnet': ('环球财经', 'http://www.chineseworldnet.com/', 0.6),
    'people': ('人民网', 'http://finance.people.com.cn/', 0.9),
    'aastocks': ('阿斯达克财经网', 'http://www.aastocks.com/', 0.7),
    'jrj': ('金融界', 'http://www.jrj.com.cn/', 1.0),
    'ftchinese': ('FT中文网', 'http://www.ftchinese.com/', 0.7),
    'cnstock': ('中国证券网', 'http://www.cnstock.com/', 0.9),
    'caijing': ('财经网', 'http://www.caijing.com.cn/', 0.8),
    'xinhuanet': ('新华网', 'http://www.xinhuanet.com/', 0.8),
    'yzforex': ('亚洲外汇网', 'http://news.yzforex.com/', 0.7),
    'cs': ('中证网', 'http://cs.com.cn/', 0.9),
    'p5w': ('全景网', 'http://www.p5w.net/', 0.9),
    'chinaipo': ('新三板在线', 'http://www.chinaipo.com/', 0.9),
    'nbd': ('每经网', 'http://www.nbd.com.cn/', 1.0),
    'nen': ('NEN财经', 'http://finance.nen.com.cn/', 0.8),
    'stockstar': ('证券之星', 'http://www.stockstar.com/', 1.0),
    'mofcom': ('中华人民共和国商务部', 'http://www.mofcom.gov.cn/', 1.0),
    'jfinfo': ('丰华财经', 'http://www.jfinfo.com/', 0.8),
    'eworldship': ('国际船舶网', 'http://www.eworldship.com/', 0.8),
    'opsteel': ('欧浦智网', 'http://www.opsteel.cn/news/', 0.7),
    'huagu': ('华股财经', 'http://www.huagu.com/', 0.8),
    'emoney': ('益盟财经', 'http://www.emoney.cn/', 0.9),
    'reuters': ('路透社中文网', 'http://cn.reuters.com/', 0.8),
    'fx678': ('汇通网', 'http://www.fx678.com/', 0.9),
    '21so': ('21财经搜索', 'http://www.21so.com/', 0.8),
    'sina': ('新浪财经', 'http://finance.sina.com.cn/', 1.0),
    'huaxi100': ('华西新闻', 'http://www.huaxi100.com/', 0.7),
    'takungpao': ('大公报', 'http://finance.takungpao.com/', 0.9),
    'eastday': ('东方网', 'http://www.eastday.com/', 0.6),
    'cnmn': ('中国有色网', 'http://www.cnmn.com.cn/', 0.7),
    'hexun': ('和讯网', 'http://www.hexun.com/', 1.0),
    'howbuy': ('好买基金网', 'http://www.howbuy.com/', 0.8),
    'stcn': ('证券时报', 'http://www.stcn.com/', 1.0),
    'jiemian': ('界面', 'http://www.jiemian.com/', 0.9),
    'ifeng': ('凤凰财经', 'http://finance.ifeng.com/', 1.0),
    'cnfol': ('中金在线', 'http://www.cnfol.com/', 0.8),
    'fx168': ('FX168财经', 'http://www.fx168.com/', 0.8),
    'yahoo': ('雅虎财经', 'https://hk.finance.yahoo.com/', 1.0),
    'zaobao': ('联合早报网', 'http://www.zaobao.com/', 0.8),
    'ceh': ('中国经济导报网', 'http://www.ceh.com.cn/', 0.7),
    'caixin': ('财新网', 'http://www.caixin.com/', 1.0),
    'wallstreetcn': ('华尔街见闻', 'http://wallstreetcn.com/', 1.0),
    'glinfo': ('钢联资讯', 'http://www.glinfo.com/', 0.7),
    'china': ('中国财经', 'http://economy.china.com/', 0.7),
    'ce': ('中国经济网', 'http://www.ce.cn/', 0.8),
    'finet': ('财华智库网', 'http://www.finet.com.cn/', 0.7),
    'gdcenn': ('中国企业新闻网', 'http://gdcenn.cn/', 0.8),
    'kxt': ('快讯通财经', 'http://www.kxt.com/news', 0.8),
    'ccstock': ('中国资本证券网', 'http://www.ccstock.cn/', 1.0),
    '591hx': ('华讯财经', 'http://www.591hx.com/', 0.9),
    'ourku': ('酷基金网', 'http://www.kjj.com/', 0.8),
    'qq': ('腾讯财经', 'http://finance.qq.com/', 1.0),
    'cnetnews': ('CNET科技资讯网', 'http://www.cnetnews.com.cn/', 0.8),
    'morningstar': ('晨星网', 'http://cn.morningstar.com/main/default.aspx', 0.8),
    '17ok': ('财界网', 'http://finance.17ok.com/', 0.8),
    '21cn': ('21CN', 'http://finance.21cn.com/', 0.9),
    '10jqka': ('同花顺', 'http://www.10jqka.com.cn/', 1.0),
    'sohu': ('搜狐财经', 'http://www.sohu.com/', 0.9),
    'qianzhan': ('前瞻网', 'http://www.qianzhan.com/', 0.85),
    'xinhua08': ('中国金融信息网', 'http://www.xinhua08.com/', 0.9),
    'eeo': ('经济观察网', 'http://www.eeo.com.cn/', 0.9),
    'cet': ('中国经济新闻网', 'http://www.cet.com.cn/', 0.8),
    'southcn': ('南方网', 'http://news.southcn.com/', 0.8),
    'thepaper': ('澎湃新闻', 'http://www.thepaper.cn/channel_25951', 1.0),
    '2258': ('2258环球财经', 'http://www.2258.com/', 0.8),
    'cailianpress': ('财联社', 'http://www.cailianpress.com/', 0.9),
    'fund123': ('数米基金网', 'http://www.fund123.cn/', 0.7),
    'chinafund': ('中国基金网', 'http://www.chinafund.cn/tree/cjzx/cjzx_1.html', 0.8),
    'chiefgroup': ('致富证券', 'http://www.chiefgroup.com.hk/', 0.7),
    'meigu18': ('美股王', 'http://www.meigu18.com/mgzx/index.html', 0.8),
    'pbc': ('中国人民银行', 'http://www.pbc.gov.cn/', 1.0),
    'cbrc': ('银监会', 'http://www.cbrc.gov.cn/chinese/home/docViewPage/110010.html', 1.0),
    'mof': ('国务院', 'http://www.gov.cn/xinwen/index.htm', 1.0),
    'huanqiu': ('环球网', 'http://finance.huanqiu.com/', 0.8),
    'kjj': ('酷基金网', 'http://news.kjj.com/', 0.8),
    'stats': ('中华人民共和国统计局', 'http://www.stats.gov.cn/', 1.0),
    '21jingji': ('21经济网', 'http://www.21jingji.com/channel/money/', 0.8),
    'eastmoney': ('东方财富网', 'http://finance.eastmoney.com/', 1.0),
    'chinanews': ('中国新闻网', 'http://finance.chinanews.com/', 0.8),
    'bwchinese': ('商业见地网', 'http://bwchinese.com/', 0.7),
    'chinaventure': ('投资中国', 'http://www.chinaventure.com.cn/', 0.9),
    'yicai': ('一财网', 'http://www.yicai.com/', 1.0),
    'asiafinance': ('亚洲财经 ', 'http://www.asiafinance.cn/jrnews/index.jspx', 0.7),
    'xsbdzw': ('中国证券报', 'http://www.xsbdzw.com/', 1.0),
    'yingfu001': ('赢富财经网', 'http://finance.yingfu001.com/', 0.9),
    'investide': ('投资潮', 'http://www.investide.cn/', 0.7),
    'capitalweek': ('证券网', 'http://www.jjckb.com/', 0.7),
    'jjckb': ('经济参考报', 'http://www.jjckb.cn/', 0.8),
    'cx368': ('中国财讯网', 'http://www.cx368.com/', 0.8),
    'pedaily': ('投资界', 'http://www.pedaily.cn/', 0.8),
    'chinadevelopment': ('中国发展网', 'http://www.chinadevelopment.com.cn/', 0.8),
    'cb': ('中国经营网', 'http://www.cb.com.cn/', 0.9),
    'zgqyzxw': ('中国前沿资讯网', 'http://www.zgqyzxw.com/', 0.7),
    'sanban18': ('新三板在线', 'http://www.chinaipo.com/', 1.0),
    'zjqiye': ('浙江企业新闻网', 'http://www.zjqiye.net/finance/', 0.7),
    'cri': ('国际在线', 'http://www.cri.cn/', 0.8),
    'sxccn': ('企业资讯网', 'http://www.sxccn.com/news/woziazai/', 0.7),
    'cntv': ('央视网', 'http://news.cctv.com/', 0.9),
    'cyzone': ('创业邦', 'http://www.cyzone.cn/', 0.7),
    'senn': ('南方企业新闻网', 'http://www.senn.com.cn/', 0.7),
    'newssc': ('四川新闻网', 'http://www.newssc.org/', 0.8),
    'zhongsou': ('中搜资讯', 'http://zixun.zhongsou.com/finance.html', 0.8),
    'oeeee': ('南都网', 'http://www.oeeee.com/', 0.6),
    'qiye': ('中国企业网', 'http://news.qiye.gov.cn/', 0.7),
    'bjnews': ('新京报网', 'http://www.bjnews.com.cn/finance/', 0.8),
    'cnenbd': ('中国企业新闻通讯社', 'http://www.cnenbd.com/', 0.7),
    'cfi': ('中财网', 'http://www.cfi.net.cn/', 0.9),
    'cnr': ('央广网', 'http://finance.cnr.cn/', 0.9),
    'huxiu': ('虎嗅网', 'https://www.huxiu.com/', 0.8),
    'mysteel': ('上海钢联网', 'http://www.mysteel.com/', 0.6),
    'haiwainet': ('海外网', 'http://www.haiwainet.cn/', 0.7),
    'news': ('新华网', 'http://www.news.cn/fortune/', 0.9),
    'gw': ('大智慧', 'http://www.gw.com.cn', 0.8),
    'rareearthinfo': ('中国稀土学会', 'http://www.rareearthinfo.com/', 0.8),
    'bbtnews': ('北京商报网', 'http://www.bbtnews.com.cn', 0.8),
    'hongzhoukan': ('红周刊', 'http://news.hongzhoukan.com', 0.8),
    'haowaicaijing': ('号外财经网', 'http://www.haowaicaijing.com/', 0.7),
    'yuncaijing': ('云财经', 'http://www.yuncaijing.com/', 0.8),
    'ofweek': ('OFweek', 'http://www.ofweek.com/', 0.7),
    'hibor': ('慧博资讯', 'http://www.hibor.com.cn/', 0.8),
    'jc001': ('九正建材网', 'http://news.jc001.cn', 0.6),
    '52steel': ('我爱钢铁网', 'http://www.52steel.com', 0.6),
    'upchina': ('优品财经', 'http://www.upchina.com/news/', 0.6),
}


def get_news_count():
    web_site = defaultdict(int)
    # client = MongoClient(['54.223.37.5'], 27017)
    client = MongoClient(['10.0.250.10'], 27017)
    collection = client['news']['crawler_news']

    from_day = date.today() - timedelta(days=1)
    to_day = date.today() - timedelta(days=7)

    excludes = ['us', '港股新闻', 'hk']
    fields = {'url': 1, 'source': 1}
    query = {'date': {
        '$lte': str(from_day).replace('-', '') + '000000',
        '$gte': str(to_day).replace('-', '') + '235959'
    }}
    print query

    for doc in collection.find(query, fields):
        source = doc['source']

        try:
            domain = get_tld(doc['url'], as_object=True).domain

            for sou in excludes:
                if sou in source:
                    break
            else:
                web_site[domain] += 1
        except:
            pass

    client.close()
    return web_site, from_day, to_day


def get_web_rank():
    result = []
    web_site, from_day, to_day = get_news_count()
    max_count = max(web_site.values())

    client = MongoClient(['10.0.250.10'], 27017)
    collection = client['news']['webrank']

    for key, val in web_site.iteritems():
        map_value = SITE_NAME_MAP.get(key, ())

        if map_value:
            result.append(map_value[:-1] + ('%.4f' % (map_value[-1] * val / max_count),))

    data = {
        'data': sorted(result, key=lambda it: it[-1], reverse=True),
        'crt': datetime.now(),
        'from': str(from_day),
        'to': str(to_day)
    }
    collection.insert(data)
    client.close()


if __name__ == '__main__':
    # app.add_job(get_web_rank, trigger='cron', hour='9', minute='30')
    app.add_job(get_web_rank, trigger='cron', hour='9')
    app.start()



