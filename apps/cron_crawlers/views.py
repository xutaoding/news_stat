# -*- coding: utf-8 -*-
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
import simplejson

from .models import PostAModel


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
        return Response(required_pdf)  # rest_error, why
