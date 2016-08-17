# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import AmazonNewsStatView
from views import QueryCatView
from views import CrawlerNewsView
from views import NewsSourceView
from views import CrawlerTotalNews
from views import AnalysisTotalNews
from views import WencaiView

urlpatterns = [
    url('^amazon/stat/data.json$', view=AmazonNewsStatView.as_view(), name='amazon_stat'),
    url('^amazon/cat/data.json$', view=QueryCatView.as_view(), name='amazon_cat'),

    url(r'^amazon/origin/data.json$', view=CrawlerNewsView.as_view(), name='amazon_origin'),
    url(r'^amazon/total/data.json$', view=CrawlerTotalNews.as_view(), name='amazon_total'),
    url(r'^amazon/source/data.json$', view=NewsSourceView.as_view(), name='amazon_source'),

    # 统计分析后的新闻总数（当天到之前的历史记录）
    url(r'^amazon/analysis_after/data.json$', view=AnalysisTotalNews.as_view(), name='amazon_analysis_after'),

    # 统计知识图谱抓取语料(问财)
    url(r'^amazon/wencai/data.json$', view=WencaiView.as_view(), name='wencai')
]

