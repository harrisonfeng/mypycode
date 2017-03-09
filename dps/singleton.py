#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Solution 1
# We check whether an instance is already created. If created, we return it;
# otherwise, we ceate an new instance, assign it to a class attribute, and 
# return it.

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# Solution 2

class Borg(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


# Solution 3

class MetaSingleton(object):
    pass


# Solution 4

def singleton(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
