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
    'patent': 'patent',
}

# Pro A Stock mongo settings
PRO_A_POST_HOST = '122.144.134.95'
PRO_A_POST_PORT = 27017
PRO_A_POST_DB = 'news'
PRO_A_POST_TABLE = 'announcement'

PRO_SCRAPYD_HOST = 'http://localhost:6800'

# count SH env
PRO_SH_HOST = '192.168.251.95'
PRO_SH_PORT = 27017
PRO_SH_ADA_DB = 'ada'
PRO_SH_NEWS_DB = 'news'
PRO_SH_TABLES = {
    'annou_us': 'announcement_us',
    'annou_hk': 'announcement_hk',
    'annou_hk_chz': 'announcement_hk_chz',
    'annou_otc': 'announcement_otc',
    'report': 'research_report_def',
    'execu': 'base_executive_regulation',
    'margin': 'base_margin_trading',
    'trade': 'base_block_trade',
}
