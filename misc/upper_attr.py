#!/usr/bin/env ptyhon
# -*- coding: utf-8 -*-

def upper_attr(future_class_name, future_class_parents, future_class_attrs):
    uppercase_attrs = {}
    for n, v in future_class_attrs.items():
        if not n.startswith('__'):
            uppercase_attrs[n.upper()] = v
        else:
            uppercase_attrs[n] = v

    return type(future_class_name, future_class_parents, uppercase_attrs)


__metaclass__ = upper_attr

class Foo():
    bar = 'foo_bar'


print hasattr(Foo, 'bar')
print hasattr(Foo, 'BAR')

f = Foo()

print f.BAR
