#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from pydecorator.libs import coroutine, time_func


if __name__ == '__main__':
    @coroutine
    @time_func
    def grep(pattern):
        print "Looking for {}".format(pattern)
        while True:
            line = (yield)
            if pattern in line:
                print line,

    g = grep("python")
    g.send("Yeah, yeah...")
    g.send("go coroutine...")
    g.send("python generator rocks")

    @time_func
    def test_time():
        time.sleep(2)

    test_time()
