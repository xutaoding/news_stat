"""news_stat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/news/', include('apps.amazon_stat.urls', namespace='amazon')),

    # So far, We don't need to `intranet`
    url(r'^api/news/', include('apps.intranet_stat.urls', namespace='intranet')),

    url(r'^api/corpus/', include('apps.corpus.urls', namespace='corpus')),
    url(r'^api/cron/', include('apps.cron_crawlers.urls', namespace='cron_crawlers')),
]
