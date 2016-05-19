from __future__ import unicode_literals

# from django.db import models
from mongoengine import *

from news_stat.settings import NEWS_HOST, NEWS_PORT, NEWS_DB, NEWS_TABLE

connect(NEWS_DB, host=NEWS_HOST, port=NEWS_PORT)


# Create your models here.
class NewsAnalysis(DynamicDocument):
    url = URLField()
    dt = StringField()
    cat = StringField()

    meta = {
        'indexes': ['dt'],
        'collection': NEWS_TABLE,
    }

