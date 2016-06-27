# -*- coding: utf-8 -*-
from datetime import datetime
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CorpusCountBaidu
from .models import CorpusCountJobs
from .models import CorpusCountGuba
from .models import CorpusCountWeixin
from .models import CorpusCountXueqiu
from .models import CorpusCountZhihu
from .models import CorpusCountComp


# Create your views here.
class ViewBase(APIView):
    @property
    def default_date(self):
        return datetime.now().strftime('%Y%m%d')

    def get(self, request):
        # date: 表示根据给定日期来统计这天的总数, 默认rtype为1
        # rtype: 2 表示统计之前所有到当前的总数， 与date无关
        query_date = request.GET.get('date', self.default_date)
        rtype = request.GET.get('rtype', '1')
        query_params = query_date.replace('-', '')

        if rtype == '1' or query_params:
            queryset = self.model_class.objects.filter(ct__startswith=query_params)

        if rtype == '2':
            queryset = self.model_class.objects.filter()
        return Response({query_params: queryset.count()})


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


