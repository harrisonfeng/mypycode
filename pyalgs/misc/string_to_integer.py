#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Leetcode: String to Integer (atoi)

'''atoi

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, 
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given 
input specs). You are responsible to gather all the input requirements up front.

Requirements for atoi:

The function first discards as many whitespace characters as necessary until 
the first non-whitespace character is found. Then, starting from this character,
takes an optional initial plus or minus sign followed by as many numerical 
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral 
, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid 
integral number, or if no such sequence exists because either str is empty or 
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the 
correct value is out of the range of representable values, INT_MAX (2147483647)
 or INT_MIN (-2147483648) is returned.
'''

# Convert a string in which all characters are digits to integer
# 1. sign '+', '-'
# 2. 000
# 3. Exceptional case, '090' will be converted to 90
def atoi(s):
    ''' Convert a string to integer

    Convert a string in which all characters are digits to integer.

    Args:
        s: the string in which all characters are digits
    Return:
        an integer 
    '''
    if len(s) <= 0:
        raise ValueError('String is empty!')
    k = 0
    flag = '+'
    if s[0] == '-' or s[0] == '+':
        flag = s[0]
        s = s[1:]
    if not s.isdigit():
        raise ValueError('Invalid chars included')
    L = len(s)
    for i, e in enumerate(s, 1):
        k += (ord(e) - ord('0')) * 10 ** (L - i)
    if flag == '-':
        k = 0 - k 
    return k

if __name__ == '__main__':
    print(atoi('000'))
    print(atoi('-123'))
    print(atoi('+120'))
    print(atoi('-0'))
