# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.db import models
from mongoengine import *

from news_stat.settings import LOG_HOST, LOG_PORT, LOG_DB, LOG_TABLE

connect(LOG_DB, alias='news_log', host=LOG_HOST, port=LOG_PORT)


# Create your models here.
class LogNewsStat(DynamicDocument):
    dt = StringField()
    count = IntField()
    dist = ListField()
    site = StringField()
    cat = DictField()

    meta = {
        # 'indexes': [('dt', 'site')],
        'db_alias': 'news_log',  # `db_alias` very important
        'collection': LOG_TABLE,
    }



