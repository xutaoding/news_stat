from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import View

from scrapyd_api import ScrapydAPI

from .models import CrawlersAPiModel
from news_stat.settings import SCRAPYD_HOST


# Create your views here.
class Base(object):
    def run_scrapy_api(self):
        spider_name = 'news'
        project = 'news_spiders'
        scrapy_host = SCRAPYD_HOST
        ScrapydAPI(target=scrapy_host).schedule(project, spider_name)


class CrawlersApiView(View, Base):
    model_class = CrawlersAPiModel

    def get(self, request):
        pass

    def post(self, request):
        pass

