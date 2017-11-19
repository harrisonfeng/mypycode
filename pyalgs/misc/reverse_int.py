#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Leetcode: Reverse digits of an integer

'''reverse_int

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Have you thought about this?

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

Throw an exception? Good, but what if throwing an exception is not an option? You would then have to re-design the function (ie, add an extra parameter).
'''

# Breakdown
# 1) integer with sign "-" or "+"
# 2) last digit is 0, e.g. 10, 10000
# 3) overflow
#
def reverse_int(n):
    sn = str(n)
    s = ''
    for i in range(len(sn) - 1 , -1, -1):
        s += sn[i]
    if s.endswith('-'):
        s = '-' + s.rstrip('-')
    return int(s)


def main():
    print(reverse_int(-123))
    print(reverse_int(100))
    print(reverse_int(0))
    print(reverse_int(92233720368547758079))

if __name__ == '__main__':
    main()
