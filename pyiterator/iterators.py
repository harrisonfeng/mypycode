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


# The class below define a __iter__ method to delegate iteration to
# the internal held container

class Node(object):

    def __init__(self, value):
        self.value = value
        self._children_nodes = list()

    def add_child(self, node):
        if node not in self._children_nodes:
            self._children_nodes.append(node)

    def __iter__(self):
        return iter(self._children_nodes)

    def __repr__(self):
        return "Node({!r})".format(self.value)
