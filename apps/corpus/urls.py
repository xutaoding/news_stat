from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^guba/data.json$', views.ViewGuba.as_view()),
    url(r'^baidu/data.json$', views.ViewBaidu.as_view()),
    url(r'^weixin/data.json$', views.ViewWeixin.as_view()),
    url(r'^xueqiu/data.json$', views.ViewXueqiu.as_view()),
    url(r'^zhihu/data.json$', views.ViewZhihu.as_view()),
    url(r'^jobs/data.json$', views.ViewJobs.as_view()),
    url(r'^comp/data.json$', views.ViewCompInfo.as_view()),

]
