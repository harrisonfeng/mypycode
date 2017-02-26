#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 删除list里重复的元素
# 1. 保留list的原有的顺序
# 2. 不保留原有的顺序

# This solution is naive approach. It suppose that elements of list are hashable 
def rm_duplicates(lst):
    '''Remove duplicates from a list
    
    >>> rm_duplicates(['a', 'b', 'b', 'c', 'd', 'a'])
    ['a', 'b', 'c', 'd']
    
    Args:
        lst: a list with hashable elements
    Return:
        a list with all unique elements
    '''
    if any(lst):
        lst.sort()
        L = len(lst)
        tail = lst[-1]
        for i in range(L-2, -1, -1):
            if lst[i] == tail:
                del lst[i]
            else:
                tail = lst[i]
        return lst

# This solution is solid solution for sequence.
def remove_duplicates(seq, key=None):
    ''' Remove duplicate items from given sequence
    
    >>> d = [{'a': 3}, {'b': 4}, {'a': 3}, {'c': 5}, {'d': 5}, {'c': 5}] 
    >>> list(remove_duplicates(d, key=lambda item: tuple(item.values()))) # python 3
    [{'a': 3}, {'b': 4}, {'c': 5}]
     
    Args:
        seq: a sequence
        key: a function to get the value of items
    Return:
        a sequence with duplicate items removed
    '''
    useq = set()
    for e in seq:
        if key == None:
            val = e
        else:
            val = key(e)
        if val not in useq:
            yield e
            useq.add(val)
