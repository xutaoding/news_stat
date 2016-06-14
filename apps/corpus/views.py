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
        query_date = request.GET.get('date', self.default_date)
        query_params = query_date.replace('-', '')
        queryset = self.model_class.objects.filter(ct__startswith=query_params)
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


