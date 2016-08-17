1：对新闻各站点的统计分析：
------------------------
URL: http://54.223.52.50:8005/api/news/amazon/stat/data.json

查询字符串参数：

date：查询起始日期，格式：yyyymmdd， 长度为8

响应格式：json

示例：
-----
http://54.223.52.50:8005/api/news/amazon/stat/data.json?date=20160520

start:
------
(54.223.52.50)
# /opt/interface/uwsgi/src/uwsgi-2.0.12/uwsgi --http :8005 --chdir /opt/interface/news_stat --module news_stat.django_uwsgi --pythonpath /opt/venv2.7.10/lib64/python2.7/site-packages
/opt/interface/uwsgi/src/uwsgi-2.0.12/uwsgi --http :8005 --chdir /opt/interface/news_stat --module news_stat.django_uwsgi -H /opt/venv2.7.10

部署环境：
1：新闻方面部署在 54.223.52.50 上面， 定时调度在192.168.250.207上
2：评论性语料部署在 192.168.250.207 上面192.168.250.207上

接口说明：
--------
1：http://54.223.52.50:8005/api/news/amazon/stat/data.json?date=20160627

说明：抓取的新闻在NLP分析后的每个站点的各类新闻的数目统计， 包括

（1）：该站点在当天的所有新闻分布

（2）：该站点的新闻分类的总数

2：http://54.223.52.50:8005/api/news/amazon/total/data.json?date=20160627

说明：抓取新闻在NLP分析之前， 且在当天和之前所有的历史的各新闻分类的统计

3：http://192.168.250.207:7900/api/corpus/{corpus}/data.json?date={date}

说明：抓取的各站点评论性语料的统计， 只统计当天抓了数目

4：http://192.168.250.207:7900/api/corpus/{corpus}/data.json?rtype=2&date={date}

说明：统计各站点当天和之前所有历史数据的统计

5：http://54.223.52.50:8005/api/news/amazon/origin/data.json?date={}

说明：当天的抓取后在NLP分析之前的各新闻分类的数据统计

6：http://54.223.52.50:8005/api/news/amazon/source/data.json

说明：各新闻分类的站点源的数目统计

7: http://54.223.52.50:8005/api/news/amazon/wencai/data.json?date=2016-08-17
说明：统计关于知识图谱抓取的数据(shuqing)

缺点：
-----
该统计API并没有根据rest_framework的model, serializers来标准化编写接口