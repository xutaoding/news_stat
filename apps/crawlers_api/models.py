from __future__ import unicode_literals

from django.db import models
from mongoengine import *

from news_stat.settings import NEWS_HOST, NEWS_PORT, NEWS_DB, CRAWLER_NEWS_TABLE

connect(NEWS_DB, alias='crawlers_api', host=NEWS_HOST, port=NEWS_PORT)


# Create your models here.
class CrawlersAPiModel(DynamicDocument):
    uid = StringField()
    title = StringField()
    content = StringField()

    meta = {
        # 'indexes': [('dt', 'site')],
        'db_alias': 'crawlers_api',  # `db_alias` very important
        'collection': CRAWLER_NEWS_TABLE,
    }
