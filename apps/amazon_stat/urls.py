from django.conf.urls import url

from views import AmazonNewsStatView
from views import QueryCatView
from views import CrawlerNewsView
from views import NewsSourceView
from views import CrawlerTotalNews

urlpatterns = [
    url('^amazon/stat/data.json$', view=AmazonNewsStatView.as_view(), name='amazon_stat'),
    url('^amazon/cat/data.json$', view=QueryCatView.as_view(), name='amazon_cat'),

    url(r'^amazon/origin/data.json$', view=CrawlerNewsView.as_view(), name='amazon_origin'),
    url(r'^amazon/total/data.json$', view=CrawlerTotalNews.as_view(), name='amazon_total'),
    url(r'^amazon/source/data.json$', view=NewsSourceView.as_view(), name='amazon_source'),
]

