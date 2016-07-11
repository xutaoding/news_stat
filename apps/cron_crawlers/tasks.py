# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task

from crawlers.shares_tianjin import Tjsoc


@shared_task
def add(x, y):
    return x + y


@shared_task
def sync_shares_tianjin():
    """ 天津股权信息的抓取, Celery 异步方式 """
    Tjsoc().main()
