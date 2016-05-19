# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import time


class Validation(object):
    success_status = 200
    type_or_size_status = 105
    error_size_status = 205

    def __init__(self, value):
        self.value = value

    def check_size(self, length=None):
        if len(self.value) != length:
            return self.type_or_size_status
        return self.success_status

    def check_date(self):
        res_size = self.check_size(8)

        if res_size != self.success_status:
            return res_size

        try:
            date_format = '%s-%s-%s' % (self.value[:4], self.value[4:6], self.value[6:])
            time.strptime(date_format, "%Y-%m-%d")
            return self.success_status
        except ValueError:
            pass
        return self.type_or_size_status

    def check_type(self):
        pass

    @staticmethod
    def compare_size(cmp_a, cmp_b):
        return Validation.success_status if cmp_a <= cmp_b else Validation.error_size_status


