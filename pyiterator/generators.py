#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


LOG = logging.getLogger(__name__)


def fib(n):

    a, b = 0, 1
    while n > a:
        yield a
        LOG.info("Yield: {0}".format(a))
        a, b = b, a + b
