#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author Harrison Feng <feng.harrison@gmail.com>
'''

import timeit


def create_string():
    return 'fuck' * 10

def concatenate_str():
    return ''.join(['fuck' for _ in xrange(10)])

def plus_str():
    s = ''
    for _ in xrange(10):
        s += 'fuck'
    return s

if __name__ == '__main__':
    t1 = timeit.Timer("create_string()", "from __main__ import create_string")
    print("multiple ", t1.timeit(10 ** 5), "milliseconds")
    t2 = timeit.Timer("concatenate_str()", "from __main__ import concatenate_str")
    print("concatenate ", t2.timeit(10 ** 5), "milliseconds")
    t3 = timeit.Timer("plus_str()", "from __main__ import plus_str")
    print("plus_str", t3.timeit(10 ** 5), "milliseconds")
