'''bubble_sort

'''

def bubble_sort(seq):
    seq_size = len(seq)
    for i in range(seq_size - 1):
        for j in range(seq_size-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]


def bubble_sort_alt(seq):
    n = len(seq)
    while(n != 0):
        for i in range(n-1):
            if(seq[i] > seq[i+1]):
                seq[i], seq[i+1] = seq[i+1], seq[i]
        n -= 1
