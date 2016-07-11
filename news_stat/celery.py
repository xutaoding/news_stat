# -*- coding: utf-8 -*-

"""
必须创建一个叫 celery.py 模块名的文件定义应用， 设置配置(在django工程的settings.py中)， 并且在__init__.py中：
        # -*- coding: utf-8 -*-
        from __future__ import absolute_import

        ''' 当启动程序的时候就会建立 Celery app 应用 '''
        from .celery import app as current_app

注意：
    django settings.py中的 DEBUG = True, 否则可能不能执行相应任务
"""

from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_stat.settings')

app = Celery('news_stat.api.cron_celery')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    """ `bind=True` 表示可以自动搜索任务(django 应用中的默认的tasks.py里定义的任务) """
    print('Request: {0!r}'.format(self.request))


