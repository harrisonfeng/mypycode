'''bubble_sort

'''
def bubble_sort_alt(seq):
    n = len(seq)
    while(n != 0):
        for i in range(n-1):
            if(seq[i] > seq[i+1]):
                seq[i], seq[i+1] = seq[i+1], seq[i]
        n -= 1

def bubble_sort(seq):
    seq_size = len(seq)
    for i in range(seq_size - 1):
        for j in range(seq_size-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    
def main():
    seq = ['9', '2', '3', '7', '0', '6', '8', '5', '4']
    bubble_sort(seq)
    print(seq == sorted(seq))
    
if __name__ == '__main__':
    main()