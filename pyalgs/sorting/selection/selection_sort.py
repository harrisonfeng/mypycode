#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging


LOG = logging.getLogger(__name__)


def selection_sort(seq):

    for i in xrange(len(seq) - 1, 0, -1):
        max_j = i
        for j in xrange(i):
            if seq[j] > seq[max_j]:
                max_j = j
            seq[i], seq[max_j] = seq[max_j], seq[i]
    return seq
