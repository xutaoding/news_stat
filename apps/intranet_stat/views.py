# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import LogNewsStat
from api import IntranetLogStat


class ViewBase(APIView):
    model_class = LogNewsStat
    default_date = str(date.today()).replace('-', '')

    @property
    def fields(self):
        return self.model_class.__dict__['_fields'].keys()


# Create your views here.
class LogNewsStatView(ViewBase):
    def get(self, request):
        query_start = request.GET.get('start', self.default_date)
        query_end = request.GET.get('end', self.default_date)

        queryset = self.model_class.objects.filter(
            dt__gte=query_start,
            dt__lte=query_end
        )

        new_queryset = [{k: docs[k] for k in self.fields} for docs in queryset]
        data = IntranetLogStat(new_queryset, self.fields, query_start, query_end).get_log_stat()
        return Response(data)


