一、北京亚马逊的相关抓取数据的统计接口
====================================
1：对新闻各站点的统计分析：
------------------------
URL: http://54.223.52.50:8005/api/news/amazon/stat/data.json

查询字符串参数：

date：查询起始日期，格式：yyyymmdd， 长度为8；

响应格式：json

示例：http://54.223.52.50:8005/api/news/amazon/stat/data.json?date=20160520

2：http://54.223.52.50:8005/api/news/amazon/total/data.json?date=20160627

说明：抓取新闻在NLP分析之前， 且在当天和之前所有的历史的各新闻分类的统计

3：http://54.223.52.50:8005/api/news/amazon/stat/data.json?date=20160627

说明：抓取的新闻在NLP分析后的每个站点的各类新闻的数目统计， 包括

（1）：该站点在当天的所有新闻分布

（2）：该站点的新闻分类的总数

4：http://54.223.52.50:8005/api/news/amazon/total/data.json?date=20160627

说明：抓取新闻在NLP分析之前， 且在当天和之前所有的历史的各新闻分类的统计

5：http://54.223.52.50:8005/api/news/amazon/origin/data.json?date={}

说明：当天的抓取后在NLP分析之前的各新闻分类的数据统计

6：http://54.223.52.50:8005/api/news/amazon/source/data.json

说明：各新闻分类的站点源的数目统计

7: http://54.223.52.50:8005/api/news/amazon/wencai/data.json?date=2016-08-17

说明：统计关于知识图谱抓取的数据(shuqing)

start:
------
(54.223.52.50)
error:/opt/interface/uwsgi/src/uwsgi-2.0.12/uwsgi --http :8005 --chdir /opt/interface/news_stat --module news_stat.django_uwsgi --pythonpath /opt/venv2.7.10/lib64/python2.7/site-packages

correct:/opt/interface/uwsgi/src/uwsgi-2.0.12/uwsgi --http :8005 --chdir /opt/interface/news_stat --module news_stat.django_uwsgi -H /opt/venv2.7.10

部署环境：
--------
1：接口部署： 54.223.52.50:/opt/interface(项目名：news_stat)，部署方式supervisor + uwsgi + django

2：定时调度： 192.168.250.207：/opt/interface/schedule（即stat项目下的 aps.py 程序文件）

3: 存储：192.168.100.15下的log库中， 具体可参照 aps.py 程序中指定的那个表里

4：所属应用：news_stat/apps/amazon_stat

二、内网根据需求的相关抓取数据的统计接口
接口说明：
--------
1：http://192.168.250.207:7900/api/corpus/{corpus}/data.json?date={date}

说明：抓取的各站点评论性语料的统计， 只统计当天抓了数目

2：http://192.168.250.207:7900/api/corpus/{corpus}/data.json?rtype=2&date={date}

说明：统计各站点当天和之前所有历史数据的统计

部署环境：
--------
1：接口部署: 192.168.250.207:/opt/interface, 部署方式supervisor + gunicorn + django

2: 定时调度：192.168.250.207：/opt/interface/schedule（即stat项目下的 aps.py 程序文件）

3：存储：192.168.100.15下的log库中， 具体可参照 aps.py 程序中指定的那个表里

4：所属应用：news_stat/apps/corpus_stat

特别说明：
=====
一和二的所属应用可能不完全， 具体参照定时调度程序(news_stat/aps.py)的代码， 查找各应用的相关urls找到匹配的接口， 即是该应用

缺点：
-----
该统计API并没有根据rest_framework的model, serializers来标准化编写接口

三：新闻网站排名：

说明：主要是根据news_spiders项目中所用到的所有财经类网站，需要将这些网站进行一个排名，写入54.223.37.5数据库

程序路径：news_stat/webrank.py

部署环境：

1：程序位置：54.223.52.50：/opt/scraper/webrank

2: 程序执行screen -ls(webrank的那个)

3：存储位置: 54.223.37.5 news -> webrank

4: 定时调度

备注：具体问题已代码为准