'''
Created on Jul 24, 2014

@author: Harrison Feng <feng.harrison@gmail.com>
'''
from collections import defaultdict

def defaultdict_example():
    pairs = {('a', 1),
             ('b', 2),
             ('c', 3)
             }
    d1 = dict()
    for k, v in pairs:
        if k not in d1:
            d1[k] = []
            d1[k].append(v)
    print(d1)
    
    d2 = defaultdict(list)
    for k, v in pairs:
        d2[k].append(v)
    print(d2)
    
if __name__ == '__main__':
    defaultdict_example()