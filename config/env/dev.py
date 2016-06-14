# Dev News mongo settings
DEV_NEWS_HOST = '192.168.250.208'
DEV_NEWS_PORT = 27017
DEV_NEWS_DB = 'news'
DEV_NEWS_TABLE = 'hotnews_analyse'

# Dev Log mongo settings
DEV_LOG_HOST = '192.168.100.20'
DEV_LOG_PORT = 27017
DEV_LOG_DB = 'log'
DEV_LOG_TABLE = 'news_stat'

DEV_CORPUS_HOST = '192.168.100.20'
DEV_CORPUS_PORT = 27017
DEV_CORPUS_DB = 'py_crawl'
DEV_CORPUS_TABLES = {
    'guba': 'guba',
    'jobs': 'jobs',
    'weixin': 'weixin',
    'xueqiu': 'xueqiu',
    'zhihu': 'zhihu',
    'baidu': 'baidu',
    'comp_info': 'comp_info',
}
