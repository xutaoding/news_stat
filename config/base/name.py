# -*- coding: utf-8 -*-
from __future__ import unicode_literals

SITE_NAME_MAP = {
    '163': '网易财经',
    'cnforex': '环球外汇',
    'chineseworldnet': '环球财经',
    'people': '人民网',
    'aastocks': '阿斯达克财经网',
    'jrj': '金融界',
    'ftchinese': 'FT中文网',
    'cnstock': '中国证券网',
    'caijing': '财经网',
    'xinhuanet': '新华网',
    'yzforex': '亚洲外汇网',
    'cs': '中证网',
    'p5w': '全景网',
    'chinaipo': '新三板在线',
    'nbd': '每经网',
    'nen': 'NEN财经',
    'stockstar': '证券之星',
    'mofcom': '中华人民共和国商务部',
    'jfinfo': '丰华财经',
    'eworldship': '国际船舶网',
    'opsteel': '欧浦智网',
    'huagu': '华股财经',
    'emoney': '益盟财经',
    'reuters': '路透社中文网',
    'fx678': '汇通网',
    '21so': '21财经搜索',
    'sina': '新浪财经',
    'huaxi100': '华西新闻',
    'takungpao': '大公报',
    'eastday': '东方网',
    'cnmn': '中国有色网',
    'hexun': '和讯网',
    'howbuy': '好买基金网',
    'stcn': '证券时报',
    'jiemian': '界面',
    'ifeng': '凤凰财经',
    'cnfol': '中金在线',
    'fx168': 'FX168财经',
    'yahoo': '雅虎财经',
    'zaobao': '联合早报网',
    'ceh': '中国经济导报网',
    'caixin': '财新网',
    'wallstreetcn': '华尔街见闻',
    'glinfo': '钢联资讯',
    'china': '中国财经',
    'ce': '中国经济网',
    'finet': '财华智库网',
    'gdcenn': '中国企业新闻网',
    'kxt': '快讯通财经',
    'ccstock': '中国资本证券网',
    '591hx': '华讯财经',
    'ourku': '酷基金网',
    'qq': '腾讯财经',
    'cnetnews': 'CNET科技资讯网',
    'morningstar': '晨星网',
    '17ok': '财界网',
    '21cn': '21CN',
    'wsj': '华尔街日报中文网',
    '10jqka': '同花顺',
    'sohu': '搜狐财经',
    'qianzhan': '前瞻网',
    'xinhua08': '中国金融信息网',
    'eeo': '经济观察网',
    'cet': '中国经济新闻网',
    'southcn': '南方网',
    'thepaper': '澎湃新闻',
    '2258': '2258环球财经',
    'cailianpress': '财联社',
    'fund123': '数米基金网',
    'chinafund': '中国基金网',
    'nytimes': '纽约时报中文网',
    'forbeschina': '福布斯中文网',
    'brandcn': '品牌中国网',
    'chiefgroup': '致富证券',
    'meigu18': '美股王',
    'pbc': '中国人民银行',
    'cbrc': '银监会',
    'mof': '国务院',
    'huanqiu': '环球网',
    'kjj': '酷基金网',
    'stats': '中华人民共和国统计局',
    '21jingji': '21经济网',
    'eastmoney': '东方财富网',
    'chinanews': '中国新闻网',
    'bwchinese': '商业见地网',
    '21cbh': '21CBH',
    'chinaventure': '投资中国',
    'yicai': '一财网',
    'asiafinance': '亚洲财经 ',
    'xsbdzw': '中国证券报',
    'yingfu001': '赢富财经网',
    'investide': '投资潮',
    'capitalweek': '证券网',
    'jjckb': '经济参考报',
    'cx368': '中国财讯网',
    'pedaily': '投资界',
    'chinadevelopment': '中国发展网',
    'cb': '中国经营网',
    'zgqyzxw': '中国前沿资讯网',
    'sanban18': '新三板在线',
    'zjqiye': '浙江企业新闻网',
    'cri': '国际在线',
    'sxccn': '企业资讯网',
    'cntv': '央视网',
    'focus': '搜狐焦点',
    'cyzone': '创业邦',
    'soufun': '搜房网',
    'pcauto': '太平洋汽车网',
    'senn': '南方企业新闻网',
    'newssc': '四川新闻网',
    'zhongsou': '中搜资讯',
    'autohome': '汽车之家',
    'cnmo': '手机中国',
    'mydrivers': '驱动之家',
    'oeeee': '南都网',
    'carnoc': '民航资源网',
    'qiye': '中国企业网',
    'bjnews': '新京报网',
    'cnenbd': '中国企业新闻通讯社',
    'cfi': '中财网',
    'gmw': '光明网',
    'loupan': '楼盘网',
    'xhby': '新华报业网',
    'cnr': '央广网 ',
    'youth': '中国青年网',
    'sootoo': '速途网',
    'hinews': '南海网',
    'chinadaily': '中国日报中文网',
    'huxiu': '虎嗅网',
    '818chuguo': '818出国网',
    'mysteel': '上海钢联网',
    'haiwainet': '海外网',
    'news': '新华网',
}

STOCK_CAT = {
    'A股新闻': {'热点新闻', '行业新闻', '宏观新闻', '股评新闻', '公司新闻'},
    '港股新闻': {'港股新闻'},
    '美股新闻': {'美股个股', '美股宏观', '美股股市', '美股行业'},
    '新三板': {'新三板'},
    '基金新闻': {'基金新闻'}
}

ORIGIN_CATEGORY = {
    'hot': 'A股新闻',
    'hjd': 'A股新闻',
    '热点新闻': 'A股新闻',
    '行业新闻': 'A股新闻',
    '宏观新闻': 'A股新闻',
    '股评新闻': 'A股新闻',
    '公司新闻': 'A股新闻',

    'hk': '港股新闻',
    '港股新闻': '港股新闻',
    '新三板': '新三板',
    '基金新闻': '基金新闻',

    'us_gg': '美股新闻',
    'us_hy': '美股新闻',
    'us_hg': '美股新闻',
    'us_gs': '美股新闻',

    'test': None,
}

NEWS_SOURCE = {
    '新三板': 12,
    '美股新闻': 21,
    '港股新闻': 16,
    '基金新闻': 17,
    'A股新闻': 80,
}
