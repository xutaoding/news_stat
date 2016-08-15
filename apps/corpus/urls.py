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

    url(r'^patent/data.json$', views.PatentViews.as_view()),
    url(r'^gibv/data.json$', views.BigvViews.as_view()),
    url(r'^etffund/data.json$', views.ETFfundViews.as_view()),
    url(r'^innotree/data.json$', views.InnotreeViews.as_view()),

    url(r'^us/data.json$', views.AnnouUsViews.as_view()),
    url(r'^hk/data.json$', views.AnnouHKViews.as_view()),
    url(r'^hk_chz/data.json$', views.AnnouHKChzViews.as_view()),
    url(r'^otc/data.json$', views.AnnouOtcViews.as_view()),
    url(r'^report/data.json$', views.AnnouReportViews.as_view()),

    url(r'^execu/data.json$', views.AnnouExecuViews.as_view()),
    url(r'^margin/data.json$', views.AnnouMarginViews.as_view()),
    url(r'^trade/data.json$', views.AnnouTradeViews.as_view()),

]
