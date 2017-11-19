'''
Created on Jul 22, 2014

@author: pygeek
'''
import unittest
import bubble_sort as bst

class Test(unittest.TestCase):

    def setUp(self):
        self.unsorted_seq = ['9', '2', '3', '7', '0', '6', '8', '5', '4']
        self.unsorted_seq_alt = self.unsorted_seq[:]

        print("Input: {0}".format(self.unsorted_seq))

        self.sorted_seq = sorted(self.unsorted_seq)
        self.sorted_seq_alt = sorted(self.unsorted_seq_alt)

        bst.bubble_sort_alt(self.unsorted_seq_alt)
        bst.bubble_sort(self.unsorted_seq)

    def tearDown(self):
        del self.unsorted_seq
        del self.unsorted_seq_alt

    def testBubbleSort(self):
        self.assertEqual(self.sorted_seq, self.unsorted_seq)
        print("Output: {0}".format(self.unsorted_seq))

    def testBubbleSortAlt(self):
        self.assertEqual(self.sorted_seq_alt, self.unsorted_seq_alt)
        print("Output alt: {0}".format(self.unsorted_seq_alt))


if __name__ == "__main__":
    unittest.main()
