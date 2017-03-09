#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time

from functools import wraps


def time_func(func):
    """Decorator to report the execution time of func.
    """
    @wraps(func)
    def time_wrapper(*args, **kwargs):
        st = time.time()
        d_func = func(*args, **kwargs)
        et = time.time()
        print "ExecutionTime: {0} is running for {1}".format(func.__name__, 
                et-st)
        return d_func
    return time_wrapper


def coroutine(func):
    """Decorator to make a coroutine starting automatically on call.
    """
    @wraps(func)
    def start(*args, **kwargs):
        d_func = func(*args, **kwargs)
        # or call send(None)
        next(d_func)
        return d_func
    return start
