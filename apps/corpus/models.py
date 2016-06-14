from __future__ import unicode_literals

# from django.db import models
from mongoengine import *

from news_stat.settings import CORPUS_HOST, CORPUS_PORT, CORPUS_DB, CORPUS_TABLES

connect(CORPUS_DB, alias='corpus', host=CORPUS_HOST, port=CORPUS_PORT)


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

