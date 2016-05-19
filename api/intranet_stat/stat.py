# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import defaultdict

from eggs import Validation, failure_msg
from config import STOCK_CAT as _STOCK


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

    def _valid_range(self):
        start = self.kwargs_date['start']
        end = self.kwargs_date['end']
        status = self._valid_date()
        cmp_status = Validation.compare_size(start, end)

        if cmp_status != Validation.success_status:
            return status or failure_msg(
                error_type=status,
                info='<start: {}, end: {}>'.format(start, end)
            )


class IntranetLogStat(StatBase):
    def __init__(self, queryset, fields, start, end):
        self.queryset = queryset
        self.fields = fields
        super(IntranetLogStat, self).__init__(start=start, end=end)

    def get_log_stat(self):
        result = defaultdict(dict)
        status_info = self._valid_range()

        if status_info:
            return status_info

        for docs in self.queryset:
            docs.pop('id')
            date_key = docs.pop('dt')
            site_key = docs.pop('site')
            docs['stock'] = {_k: 0 for _k in _STOCK}

            for key, value in docs['cat'].iteritems():
                key = key.strip()

                for _key, _value in _STOCK.iteritems():
                    if key in _value:
                        docs['stock'][_key] += value

            result[date_key][site_key] = docs
        return result

