from django.conf.urls import url

from .views import LogNewsStatView

urlpatterns = [
    url(r'^intranet/stat/data.json$', view=LogNewsStatView.as_view(), name='intranet_stat'),
]


