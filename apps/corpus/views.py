# -*- coding: utf-8 -*-
import json
from datetime import datetime
# from django.shortcuts import render
# from rest_framework.views import APIView
from django.views.generic import View as APIView
from django.http.response import HttpResponse as Response
# from rest_framework.response import Response

from mongoengine.queryset.visitor import Q

from .models import CorpusCountBaidu
from .models import CorpusCountJobs
from .models import CorpusCountGuba
from .models import CorpusCountWeixin
from .models import CorpusCountXueqiu
from .models import CorpusCountZhihu
from .models import CorpusCountComp
from . import models


# Create your views here.
class ViewBase(APIView):
    model_class = None

    def __init__(self, **kwargs):
        super(ViewBase, self).__init__(**kwargs)

    @property
    def default_date(self):
        return datetime.now().strftime('%Y%m%d')

    @staticmethod
    def to_datetime(query_string):
        """
        Convert sting to datetime
        :param query_string: string, format:20160815
        :return:
        """
        convert = (lambda dt: [int(dt[:4]), int(dt[4:6]), int(dt[6:8])])
        dt_args = convert(query_string)
        return datetime(*dt_args), datetime(*dt_args, hour=23, minute=59, second=59)

    def get(self, request):
        # date: 表示根据给定日期来统计这天的总数, 默认rtype为1
        # rtype: 2 表示统计之前所有到当前的总数
        query_date = request.GET.get('date', self.default_date)
        rtype = request.GET.get('rtype', '1')
        query_params = query_date.replace('-', '')
        dt_from, dt_to = self.to_datetime(query_params)

        if rtype == '1':
            if getattr(self, '_SH', None) is True:
                print 'dt:', dt_from, dt_to
                queryset = self.model_class.objects.filter(crt__gte=dt_from, crt__lte=dt_to)
                # queryset = self.model_class.objects.filter(__raw__={'crt': {'$gte': dt_from, '$lte': dt_to}})
            else:
                queryset = self.model_class.objects.filter(ct__startswith=query_params)

        if rtype == '2':
            if getattr(self, '_SH', None) is True:
                queryset = self.model_class.objects.filter()
            else:
                queryset = self.model_class.objects.filter(ct__lte=query_params + '235959')
        data = json.dumps({query_params: queryset.count()})
        return Response(data)


class ViewBaidu(ViewBase):
    model_class = CorpusCountBaidu


class ViewJobs(ViewBase):
    model_class = CorpusCountJobs


class ViewGuba(ViewBase):
    model_class = CorpusCountGuba


class ViewWeixin(ViewBase):
    model_class = CorpusCountWeixin


class ViewXueqiu(ViewBase):
    model_class = CorpusCountXueqiu


class ViewZhihu(ViewBase):
    model_class = CorpusCountZhihu


class ViewCompInfo(ViewBase):
    model_class = CorpusCountComp


class PatentViews(ViewBase):
    model_class = models.CorpusCountPatent


class BigvViews(ViewBase):
    model_class = models.CorpusCountBigv


class ETFfundViews(ViewBase):
    model_class = models.CorpusCountETFfund


class InnotreeViews(ViewBase):
    model_class = models.CorpusCountInnotree


class AnnouUsViews(ViewBase):
    _SH = True
    model_class = models.SHCorpusAnnouUs


class AnnouHKViews(ViewBase):
    _SH = True
    model_class = models.SHCorpusAnnouHk


class AnnouHKChzViews(ViewBase):
    _SH = True
    model_class = models.SHCorpusAnnouHkChz


class AnnouOtcViews(ViewBase):
    _SH = True
    model_class = models.SHCorpusAnnouOtc


class AnnouReportViews(ViewBase):
    _SH = True
    model_class = models.SHCorpusAnnouReport


class AnnouExecuViews(ViewBase):
    _SH = True
    model_class = models.SHCorpusAnnouExecu


class AnnouMarginViews(ViewBase):
    _SH = True
    model_class = models.SHCorpusAnnouMargin


class AnnouTradeViews(ViewBase):
    _SH = True
    model_class = models.SHCorpusAnnouTrade
