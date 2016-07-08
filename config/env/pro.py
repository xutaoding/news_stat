# Pro News mongo settings
PRO_NEWS_HOST = '10.0.250.10'
PRO_NEWS_PORT = 27017
PRO_NEWS_DB = 'news'
PRO_NEWS_TABLE = 'hotnews_analyse'
PRO_CRAWLER_NEWS_TABLE = 'crawler_news'

# Pro Log mongo settings
PRO_LOG_HOST = '192.168.100.15'
PRO_LOG_PORT = 27017
PRO_LOG_DB = 'log'
PRO_LOG_TABLE = 'news_stat'

PRO_CORPUS_HOST = '192.168.100.20'
PRO_CORPUS_PORT = 27017
PRO_CORPUS_DB = 'py_crawl'
PRO_CORPUS_TABLES = {
    'guba': 'guba',
    'jobs': 'jobs',
    'weixin': 'weixin',
    'xueqiu': 'xueqiu',
    'zhihu': 'zhihu',
    'baidu': 'baidu',
    'comp_info': 'comp_info',
}

# Pro A Stock mongo settings
PRO_A_POST_HOST = '122.144.134.95'
PRO_A_POST_PORT = 27017
PRO_A_POST_DB = 'news'
PRO_A_POST_TABLE = 'announcement'
