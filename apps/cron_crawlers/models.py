# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *

from news_stat.settings import A_POST_HOST, A_POST_PORT, A_POST_DB, A_POST_TABLE

connect(A_POST_DB, alias='sh_mongo95', host=A_POST_HOST, port=A_POST_PORT)


# Create your models here.
class PostAModel(DynamicDocument):
    """上海mongo95数据库模型"""

    title = StringField()
    file = DictField()

    meta = {
        'db_alias': 'sh_mongo95',
        'collection': A_POST_TABLE
    }

    def __unicode__(self):
        return u'%s' % self.title
