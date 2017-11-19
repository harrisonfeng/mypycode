#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging


LOG = logging.getLogger(__name__)


def insertion_sort(seq):

    for i in xrange(1, len(seq)):
        cur_val = seq[i]
        pos = i

        while pos > 0  and seq[pos-1] > cur_val:
            seq[pos] = seq[pos-1]
            pos = pos - 1

        seq[pos] = cur_val
