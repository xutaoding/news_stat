from django.conf.urls import url

from views import AmazonNewsStatView
from views import QueryCatView

urlpatterns = [
    url('^amazon/stat/data.json$', view=AmazonNewsStatView.as_view(), name='amazon_stat'),
    url('^amazon/cat/data.json$', view=QueryCatView.as_view(), name='amazon_cat')
]

