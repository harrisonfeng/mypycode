#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author Harrison Feng <feng.harrison@gmail.com>
'''

import timeit


def string_multi():
    return 'fuck' * 100

def string_join():
    return ''.join(['fuck' for _ in xrange(100)])

def string_plus():
    s = ''
    for _ in xrange(100):
        s += 'fuck'
    return s

if __name__ == '__main__':
    t1 = timeit.Timer("string_multi()", "from __main__ import string_multi")
    print("multiple ", t1.timeit(10 ** 5), "milliseconds")
    t2 = timeit.Timer("string_join()", "from __main__ import string_join")
    print("join ", t2.timeit(10 ** 5), "milliseconds")
    t3 = timeit.Timer("string_plus()", "from __main__ import string_plus")
    print("plus ", t3.timeit(10 ** 5), "milliseconds")
