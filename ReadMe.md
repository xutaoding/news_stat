1：对新闻各站点的统计分析：
------------------------
URL: http://127.0.0.1:8005/api/news/amazon/stat/data.json

查询字符串参数：

date：查询起始日期，格式：yyyymmdd， 长度为8

响应格式：json

示例：
-----
http://54.223.52.50:7900/news/api/data.json?date=20160520

start:
------
(54.223.52.50)
# /opt/interface/uwsgi/src/uwsgi-2.0.12/uwsgi --http :8005 --chdir /opt/interface/news_stat --module news_stat.django_uwsgi --pythonpath /opt/venv2.7.10/lib64/python2.7/site-packages
/opt/interface/uwsgi/src/uwsgi-2.0.12/uwsgi --http :8005 --chdir /opt/interface/news_stat --module news_stat.django_uwsgi -H /opt/venv2.7.10