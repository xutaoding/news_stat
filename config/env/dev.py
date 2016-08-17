# Dev News mongo settings
DEV_NEWS_HOST = '192.168.250.208'
DEV_NEWS_PORT = 27017
DEV_NEWS_DB = 'news'
DEV_NEWS_TABLE = 'hotnews_analyse'
DEV_CRAWLER_NEWS_TABLE = 'crawler_news'

DEV_GRAPH_CRAWLER_DB = 'graph'
DEV_GRAPH_CRAWLER_TABLE = 'nlp_event'

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
    'patent': 'patent',
    'bigv': 'bigv_cubes',
    'etfund': 'etfund',
    'innotree': 'innotree',
}

# Dev A Stock mongo settings
DEV_A_POST_HOST = '122.144.134.95'
DEV_A_POST_PORT = 27017
DEV_A_POST_DB = 'news'
DEV_A_POST_TABLE = 'announcement'

DEV_SCRAPYD_HOST = 'http://192.168.250.207:6800'

# count SH env
DEV_SH_HOST = '122.144.134.95'
DEV_SH_PORT = 27017
DEV_SH_ADA_DB = 'ada'
DEV_SH_NEWS_DB = 'news'
DEV_SH_TABLES = {
    'annou_us': 'announcement_us',
    'annou_hk': 'announcement_hk',
    'annou_hk_chz': 'announcement_hk_chz',
    'annou_otc': 'announcement_otc',
    'execu': 'base_executive_regulation',
    'margin': 'base_margin_trading',
    'trade': 'base_block_trade',
    'report': 'research_report_def',
}

