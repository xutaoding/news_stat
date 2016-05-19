# -*- coding: utf-8 -*-
# from django.shortcuts import render
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response

from eggs import get_date_range
from models import NewsAnalysis
from api import AmazonNewsStat, QueryCatStat, StatBase


class NewsBase(APIView):
    model_class = NewsAnalysis
    default_date = str(date.today()).replace('-', '')

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
