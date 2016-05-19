# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import defaultdict
from datetime import datetime, timedelta

from tld import get_tld

from eggs import failure_msg, Validation
from config import SITE_NAME_MAP as _SNM, STOCK_CAT as _STOCK


class StatBase(object):
    def __init__(self, **kwargs_date):
        self.kwargs_date = kwargs_date

    def _valid_date(self):
        for key, query_date in self.kwargs_date.iteritems():
            status = Validation(query_date).check_date()

            if status != Validation.success_status:
                return failure_msg(
                    error_type=status,
                    info='<{}: {}>'.format(key, query_date)
                )

    def valid_range(self):
        start = self.kwargs_date['start']
        end = self.kwargs_date['end']
        status = self._valid_date()
        cmp_status = Validation.compare_size(start, end)

        if cmp_status != Validation.success_status:
            return status or failure_msg(
                error_type=cmp_status,
                info='<start: {}, end: {}>'.format(start, end)
            )


class AmazonNewsStat(StatBase):
    def __init__(self, queryset, query_date):
        self.queryset = queryset
        self.query_date = query_date
        super(AmazonNewsStat, self).__init__(query_date = query_date)

    @staticmethod
    def convert_dt(date_s):
        y, mon, d = date_s[:4], date_s[4:6], date_s[6:8]
        h, minute = (date_s[8:10], date_s[10:12]) if len(date_s) == 14 else (0, 0)
        return datetime(year=int(y), month=int(mon), day=int(d), hour=int(h), minute=int(minute))

    def get_dist(self, dt_list):
        interval = 30
        default_dist_len = 48
        dist_dt = [0 for _ in range(default_dist_len)]
        t_y, t_m, t_d = self.query_date[:4], self.query_date[4:6], self.query_date[6:]
        query = datetime(year=int(t_y), month=int(t_m), day=int(t_d), hour=0, minute=0)

        for _query_dt in dt_list:
            normal_dt = self.convert_dt(_query_dt)

            for index in range(default_dist_len):
                start = query + timedelta(minutes=index * interval)
                end = query + timedelta(minutes=(index + 1) * interval + 1)

                if start <= normal_dt < end:
                    dist_dt[index] += 1
                    break
        return dist_dt

    def get_news_stat(self):
        dist_key, count_key = 'dist', 'count'
        status_info = self._valid_date()
        result = defaultdict(lambda: defaultdict(int))

        if status_info:
            return status_info

        for docs in self.queryset:
            cat_key = docs['cat'].strip()

            try:
                domain = get_tld(docs['url'], as_object=True).domain
                site_name = _SNM.get(domain, domain)
                result[site_name].setdefault(dist_key, []).append(docs['dt'])
                result[site_name].setdefault('cat', defaultdict(int))

                result[site_name][count_key] += 1
                result[site_name]['cat'][cat_key] += 1
                result[site_name]['dt'] = self.convert_dt(self.query_date).strftime('%Y-%m-%d')
            except(KeyError, ValueError):
                pass
            else:
                result[site_name]['stock'] = {_k: 0 for _k in _STOCK}

                for _key, _value in result[site_name]['cat'].iteritems():
                    for site_key, values in _STOCK.iteritems():
                        if _key in values:
                            result[site_name]['stock'][site_key] += _value

        for _site_name in result:
            result[_site_name][dist_key] = self.get_dist(result[_site_name][dist_key])
        return result


class QueryCatStat(StatBase):
    def __init__(self, queryset, query_cat, start, end):
        self.queryset = queryset
        self.query_cat = query_cat
        super(QueryCatStat, self).__init__(start=start, end=end)

    def get_cat_stat(self):
        status_info = self.valid_range()
        result = {self.query_cat: defaultdict(int), 'count': 0}

        if status_info:
            return status_info

        for docs in self.queryset:
            try:
                docs_cat = docs['cat']
                domain = get_tld(docs['url'], as_object=True).domain
                site_name = _SNM.get(domain, domain)

                if docs_cat == self.query_cat:
                    result['count'] += 1
                    result[self.query_cat][site_name] += 1
            except(KeyError, ValueError):
                pass
        return result

