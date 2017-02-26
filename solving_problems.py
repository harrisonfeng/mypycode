'''
This module is a collection of solutions on a variety of problems.
These problem may be small, tiny or naive, but need to some tricks 
to solve them, 
'''
# Write a function that determines if a string 
# starts with an upper-case letter A-Z
def is_captialize(s):
    if s:
        return ord(s[0]) in range(ord('A'), ord('Z') + 1, 1)

def reverse_int(n):
    sn = str(n)
    s = ''
    for i in range(len(sn) - 1 , -1, -1):
        s += sn[i]
    if s.endswith('-'):
        s = '-' + s.rstrip('-')
    return int(s) 

def cartesian_prod(s, t):
    '''
    input: s = '*'
           t = ('a', 'b', 'c')
    output:
          [('*', '*', '*'), ('*', '*', 'c'), ('*', 'b', '*'), 
           ('*', 'b', 'c'), ('a', '*', '*'), ('a', '*', 'c'), 
           ('a', 'b', '*'), ('a', 'b', 'c')]
    '''
    import itertools
    return (itertools.product(*((s, x) for x in t)))

def reverse_word(s):
    '''
    input: "the       blue   sky"
    output: "Eht Eulb Yks"
    '''
    if(len(s) <= 0):
        raise ValueError("invalid argument")
    return ' '.join((w[::-1].capitalize() for w in s.split()))

def rm_duplicates(seq, key=None):
    '''
    '''
    unique_seqs = set()
    for e in seq:
        if key is None:
            val = e        # hashable
        else:
            val = key(e)   # unhashable
        if val not in unique_seqs:
            yield e
            unique_seqs.add(val)

def rm_duplicates_unodered(lst):
    '''
    '''
    if any(lst):
        lst.sort()
        last = lst[-1]
        for i in range(len(lst)-2, -1, -1):
            if last == lst[i]:
                del lst[i]
            else:
                last = lst[i]

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

# Convert letters to upper or lower case contained in a string 

def main():
    print(reverse_int(-12))
    print(reverse_int(100))
    print(reverse_int(1001))
    print(reverse_int(-2346))
    print(atoi('0'))
    
if __name__ == "__main__":
    main()