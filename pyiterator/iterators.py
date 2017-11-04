#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


LOG = logging.getLogger(__name__)

class Fib(object):

    def __init__(self, n):

        if not isinstance(n, int) or n < 0:
            raise TypeError('An postive integer is required.')
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):

        return self

    def next(self):

        fib = self.a

        if fib > self.n:
            raise StopIteration

        self.a, self.b = self.b, self.a + self.b
        LOG.info('\na: {0}\nb: {1}'.format(self.a, self.b))

        return fib


class CustRange(object):

    def __init__(self, n):

        if not isinstance(n, int):
            raise TypeError('An integer is required.')

        self.n = n
        self.cur = 0

    def __iter__(self):

        return self


    def next(self):

        item = self.cur
        if self.cur >= self.n:
            raise StopIteration
        self.cur += 1

        return item
