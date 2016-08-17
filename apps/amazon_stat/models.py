from __future__ import unicode_literals

# from django.db import models
from mongoengine import *

from news_stat.settings import NEWS_HOST, NEWS_PORT, NEWS_DB, NEWS_TABLE, CRAWLER_NEWS_TABLE
from news_stat.settings import GRAPH_CRAWLER_DB, GRAPH_CRAWLER_TABLE

connect(NEWS_DB, host=NEWS_HOST, port=NEWS_PORT)
connect(GRAPH_CRAWLER_DB, alias='graph', host=NEWS_HOST, port=NEWS_PORT)


# Create your models here.
class NewsAnalysis(DynamicDocument):
    url = URLField()
    dt = StringField()
    cat = StringField()

    meta = {
        'indexes': ['dt'],
        'collection': NEWS_TABLE,
    }


class CrawlerNews(DynamicDocument):
    url = URLField()
    d = StringField()
    source = StringField()
    crt = StringField(max_length=14)

    meta = {
        'indexes': ['d'],
        'collection': CRAWLER_NEWS_TABLE,
    }


class WencaiModel(DynamicDocument):
    ct = StringField()

    meta = {
        'indexes': ['ct'],
        'db_alias': 'graph',
        'collection': GRAPH_CRAWLER_TABLE,
    }

