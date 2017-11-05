#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging


LOG = logging.getLogger(__name__)

def partition(seq):

    pi, seq_new = seq[0], seq[1:]

    lo = [i for i in seq_new if i < pi]
    hi = [i for i in seq_new if i > pi]

    return lo, pi, hi

def quick_sort(seq):

    if len(seq) < 2:
        return seq

    lo, pi, hi = partition(seq)

    LOG.debug('Seq: {0}'.format(seq))
    return quick_sort(lo) + [pi] + quick_sort(hi)


def quick_sort_alt(seq):

    if len(seq) < 2:
        return seq

    pivot = len(seq) // 2
    pivot_item = seq[pivot]
    seq_new = seq[:pivot] + seq[pivot+1:]

    lo = [ i for i in seq_new if i < pivot_item]
    hi = [ i for i in seq_new if i > pivot_item]

    LOG.debug('Seq: {0}'.format(seq))
    return quick_sort_alt(lo) + [pivot_item] + quick_sort_alt(hi)
