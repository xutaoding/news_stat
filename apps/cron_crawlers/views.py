# -*- coding: utf-8 -*-
import json
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PostAModel
import tasks


# Create your views here.
def test(request):
    return HttpResponse('test ok')


class PostInfoView(APIView):
    """ 从上海环境mongo95上获取A股公告的信息 """
    model_class = PostAModel

    @staticmethod
    def _query(query_date):
        if query_date is None:
            now = datetime.now()
        else:
            now = datetime(*[int(_dt) for _dt in query_date.split('-')])

        query = {
            'pdt__gte': datetime(now.year, now.month, now.day),
            'pdt__lte': datetime(now.year, now.month, now.day, 23, 59, 59),
        }
        return query

    def get(self, request):
        required_pdf = []
        query = self._query(request.GET.get('date'))
        queryset = self.model_class.objects.filter(**query).fields(title=True, file=True)

        for post_inst in queryset:
            file_info = post_inst.file
            need_docs = {'ext': file_info['ext'], 'fn': file_info['fn'], 'url': file_info['url']}
            need_docs.update(_id=str(post_inst.id), title=post_inst.title)
            required_pdf.append(need_docs)
        # return HttpResponse(simplejson.dumps(required_pdf))
        # return Response(required_pdf)  # rest_error, why
        return Response(json.dumps(required_pdf))  


class SharesTianjinView(APIView):
    """ 异步执行抓取， 请求一次浏览器可以实现抓取 """

    def get(self, request):
        tasks.sync_shares_tianjin.delay()
        return Response(data='抓取已在进行， 请耐心等待邮件!<br /><h2>注意：请求一次即可， 请勿多次请求</h2>')

