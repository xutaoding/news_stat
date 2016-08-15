from __future__ import unicode_literals

# from django.db import models
from mongoengine import *

from news_stat.settings import CORPUS_HOST, CORPUS_PORT, CORPUS_DB, CORPUS_TABLES
from news_stat.settings import SH_CORPUS_HOST, SH_CORPUS_PORT, SH_CORPUS_ADA, SH_CORPUS_NEWS, SH_CORPUS_TABLES

connect(CORPUS_DB, alias='corpus', host=CORPUS_HOST, port=CORPUS_PORT)
connect(SH_CORPUS_ADA, alias='sh_ada', host=SH_CORPUS_HOST, port=SH_CORPUS_PORT)
connect(SH_CORPUS_NEWS, alias='sh_news', host=SH_CORPUS_HOST, port=SH_CORPUS_PORT)


# Create your models here.
class CorpusCountBaidu(DynamicDocument):
    collection_name = 'baidu'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name],
    }


class CorpusCountJobs(DynamicDocument):
    collection_name = 'jobs'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name],
    }


class CorpusCountWeixin(DynamicDocument):
    collection_name = 'weixin'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name],
    }


class CorpusCountXueqiu(DynamicDocument):
    collection_name = 'xueqiu'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name],
    }


class CorpusCountZhihu(DynamicDocument):
    collection_name = 'zhihu'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name],
    }


class CorpusCountGuba(DynamicDocument):
    collection_name = 'guba'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name],
    }


class CorpusCountComp(DynamicDocument):
    collection_name = 'comp_info'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name],
    }


class CorpusCountPatent(DynamicDocument):
    collection_name = 'patent'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name]
    }


class CorpusCountBigv(DynamicDocument):
    collection_name = 'bigv'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name]
    }


class CorpusCountETFfund(DynamicDocument):
    collection_name = 'etfund'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name]
    }


class CorpusCountInnotree(DynamicDocument):
    collection_name = 'innotree'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'corpus',
        'collection': CORPUS_TABLES[collection_name]
    }


class SHCorpusAnnouUs(DynamicDocument):
    collection_name = 'annou_us'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'sh_news',
        'collection': SH_CORPUS_TABLES[collection_name]
    }


class SHCorpusAnnouHk(DynamicDocument):
    collection_name = 'annou_hk'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'sh_news',
        'collection': SH_CORPUS_TABLES[collection_name]
    }


class SHCorpusAnnouHkChz(DynamicDocument):
    collection_name = 'annou_hk_chz'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'sh_news',
        'collection': SH_CORPUS_TABLES[collection_name]
    }


class SHCorpusAnnouOtc(DynamicDocument):
    collection_name = 'annou_otc'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'sh_news',
        'collection': SH_CORPUS_TABLES[collection_name]
    }


class SHCorpusAnnouReport(DynamicDocument):
    collection_name = 'report'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'sh_news',
        'collection': SH_CORPUS_TABLES[collection_name]
    }


class SHCorpusAnnouExecu(DynamicDocument):
    collection_name = 'execu'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'sh_ada',
        'collection': SH_CORPUS_TABLES[collection_name]
    }


class SHCorpusAnnouMargin(DynamicDocument):
    collection_name = 'margin'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'sh_ada',
        'collection': SH_CORPUS_TABLES[collection_name]
    }


class SHCorpusAnnouTrade(DynamicDocument):
    collection_name = 'trade'

    ct = StringField(max_length=14)

    meta = {
        'indexes': ['ct'],
        'db_alias': 'sh_ada',
        'collection': SH_CORPUS_TABLES[collection_name]
    }


