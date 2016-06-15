from eggs import deploy_ip

from .env.dev import DEV_NEWS_HOST, DEV_NEWS_PORT, DEV_NEWS_DB, DEV_NEWS_TABLE, DEV_CRAWLER_NEWS_TABLE
from .env.dev import DEV_LOG_HOST, DEV_LOG_PORT, DEV_LOG_DB, DEV_LOG_TABLE
from .env.dev import DEV_CORPUS_HOST, DEV_CORPUS_PORT, DEV_CORPUS_DB, DEV_CORPUS_TABLES

from .env.pro import PRO_NEWS_HOST, PRO_NEWS_PORT, PRO_NEWS_DB, PRO_NEWS_TABLE, PRO_CRAWLER_NEWS_TABLE
from .env.pro import PRO_LOG_HOST, PRO_LOG_PORT, PRO_LOG_DB, PRO_LOG_TABLE
from .env.pro import PRO_CORPUS_HOST, PRO_CORPUS_DB, PRO_CORPUS_PORT, PRO_CORPUS_TABLES

from .base.name import SITE_NAME_MAP, STOCK_CAT, ORIGIN_CATEGORY, NEWS_SOURCE

_PRO_IP = []  # Development Environment
_DEV_IP = ['192.168.1.22', '192.168.100.20', ]  # Test Environment

if deploy_ip in _DEV_IP:
    NEWS_HOST = DEV_NEWS_HOST
    NEWS_PORT = DEV_NEWS_PORT
    NEWS_DB = DEV_NEWS_DB
    NEWS_TABLE = DEV_NEWS_TABLE
    CRAWLER_NEWS_TABLE = DEV_CRAWLER_NEWS_TABLE

    LOG_HOST = DEV_LOG_HOST
    LOG_PORT = DEV_LOG_PORT
    LOG_DB = DEV_LOG_DB
    LOG_TABLE = DEV_LOG_TABLE

    CORPUS_HOST = DEV_CORPUS_HOST
    CORPUS_PORT = DEV_CORPUS_PORT
    CORPUS_DB = DEV_CORPUS_DB
    CORPUS_TABLES = DEV_CORPUS_TABLES
else:
    NEWS_HOST = PRO_NEWS_HOST
    NEWS_PORT = PRO_NEWS_PORT
    NEWS_DB = PRO_NEWS_DB
    NEWS_TABLE = PRO_NEWS_TABLE
    CRAWLER_NEWS_TABLE = PRO_CRAWLER_NEWS_TABLE

    LOG_HOST = PRO_LOG_HOST
    LOG_PORT = PRO_LOG_PORT
    LOG_DB = PRO_LOG_DB
    LOG_TABLE = PRO_LOG_TABLE

    CORPUS_HOST = PRO_CORPUS_HOST
    CORPUS_PORT = PRO_CORPUS_PORT
    CORPUS_DB = PRO_CORPUS_DB
    CORPUS_TABLES = PRO_CORPUS_TABLES
