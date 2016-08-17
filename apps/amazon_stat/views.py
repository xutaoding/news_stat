# -*- coding: utf-8 -*-
# from django.shortcuts import render
import re
import json
from collections import defaultdict

from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response

from eggs import get_date_range
from models import NewsAnalysis, CrawlerNews, WencaiModel
from api import StatBase
from api import AmazonNewsStat, QueryCatStat
from api import CrawlerNewsStat
from config import ORIGIN_CATEGORY as _NEWS_CATE


class NewsBase(APIView):
    model_class = NewsAnalysis

    @property
    def default_date(self):
        return str(date.today()).replace('-', '')

    @property
    def fields(self):
        return self.model_class.__dict__['_fields'].keys()

    @staticmethod
    def _valid_params(params, expected_params=()):
        failure_params = []

        for param in params:
            if param not in expected_params:
                failure_params.append('`%s`' % param)

        if failure_params:
            expected = ['`%s`' % p for p in expected_params]
            return {
                'status': 200,
                'info': 'failure parameters: <%s>, expect: <%s>' % (' '.join(failure_params), ' '.join(expected))
            }

    @property
    def news_categories(self):
        categories = defaultdict(list)

        for key, value in _NEWS_CATE.iteritems():
            if value:
                categories[value].append(key)
        return categories


# Create your views here.
class AmazonNewsStatView(NewsBase):
    def get(self, request):
        expected_args = 'date'
        info = self._valid_params(request.GET.keys(), expected_params=(expected_args, ))

        if info is not None:
            return Response(info)

        query_date = request.GET.get(expected_args, self.default_date)
        queryset = self.model_class.objects.filter(
            dt__gte=query_date + '000000',
            dt__lte=query_date + '235959'
        ).fields(**{k: 1 for k in self.fields})

        new_queryset = [{k: docs[k] for k in self.fields} for docs in queryset]
        data = AmazonNewsStat(new_queryset, query_date).get_news_stat()
        return Response(data)


class QueryCatView(NewsBase):
    default_cat = u'热点新闻'

    def get(self, request):
        expected_args = ('cat', 'start', 'end')
        query_cat = request.GET.get('cat', self.default_cat)
        query_start = request.GET.get('start', self.default_date)
        query_end = request.GET.get('end', self.default_date)

        info = self._valid_params(request.GET.keys(), expected_params=expected_args)
        date_status = StatBase(start=query_start, end=query_end).valid_range()

        if info is not None or date_status is not None:
            return Response(info or date_status)

        date_range = get_date_range(query_start, query_end)
        queryset = self.model_class.objects.filter(
            cat=query_cat,
            dt__gte=date_range[0] + '000000',
            dt__lte=date_range[-1] + '235959'
        ).fields(**{k: 1 for k in self.fields})

        new_queryset = [{k: docs[k] for k in self.fields} for docs in queryset]
        data = QueryCatStat(new_queryset, query_cat, query_start, query_end).get_cat_stat()
        return Response(data)


class CrawlerNewsView(NewsBase):
    model_class = CrawlerNews

    def get(self, request):
        expected_param = 'date'
        info = self._valid_params(request.GET.keys(), expected_params=(expected_param, ))

        if info is not None:
            return Response(info)

        fields = self.fields
        fields.remove('id')

        query_date = request.GET.get(expected_param)
        obj_kwargs = {'d': query_date} if query_date else {}
        queryset = self.model_class.objects.filter(**obj_kwargs).fields(**{k: 1 for k in fields})

        new_queryset = [{k: docs[k] for k in fields} for docs in queryset]
        data = CrawlerNewsStat(new_queryset, query_date).get_crawler_news_stat()
        return Response(data)


class CrawlerTotalNews(NewsBase):
    model_class = CrawlerNews

    def get(self, request):
        categories = self.news_categories
        query_date = request.GET.get('date', self.default_date).replace('-', '')
        data = {'dt': query_date}
        print query_date

        for news_cat, values in categories.iteritems():
            queryset = self.model_class.objects.filter(d__lte=query_date + '235959', source__in=values)
            data[news_cat] = queryset.count()
        return Response(data=data)


class NewsSourceView(NewsBase):
    model_class = CrawlerNews

    def get(self, request):
        data = CrawlerNewsStat(queryset=[]).get_news_source_count()
        print data
        return Response(data)


class AnalysisTotalNews(NewsBase):
    """
    统计分信后的新闻数据：从当天开始到之前的所有的历史数据
    """
    def get(self, request):
        query_date = request.GET.get('date', self.default_date)
        query_param = query_date.replace('-', '')
        data = {'dt': query_param}
        total_queryset = self.model_class.objects.filter(dt__lte=query_param + '235959')

        for key, values in self.news_categories.items():
            queryset = total_queryset(cat__in=values)
            data[key] = queryset.count()
        return Response(data=data)


class WencaiView(NewsBase):
    """  统计抓取问财数据， 关于知识图谱 """

    model_class = WencaiModel

    def get(self, request):
        query_date = request.GET.get('date', self.default_date)
        query_param = query_date.replace('-', '')

        if re.compile(r'\d{4}-\d\d-\d\d').search(query_date) is None:
            return Response("{'error': 'params <date> error'}")

        data = {
            'dt': query_date,
            'total_count': self.model_class.objects.filter().count(),
            'count': self.model_class.objects.filter(ct__startswith=query_param).count()
        }
        return Response(data=data)


