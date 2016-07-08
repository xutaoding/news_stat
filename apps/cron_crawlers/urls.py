from django.conf.urls import url

from .views import test
from .views import PostInfoView

urlpatterns = [
    url(r'^test/', test, name='test'),

    url(r'^mongo_info/95/$', PostInfoView.as_view(), name='post_a'),
]

