# -*- coding: utf-8 -*-
from __future__ import absolute_import

""" 当启动程序的时候就会建立 Celery app 应用 """
from .celery import app as current_app
