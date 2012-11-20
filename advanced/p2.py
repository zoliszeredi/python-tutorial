"""
Problem 2
Write a generator that returns all the subsets of a given set.
"""

import unittest
import itertools

def subset_generator(its_set):
    its_size = len(its_set)
    for dim in range(its_size+1):
        for elem in itertools.combinations(its_set, dim):
            yield set(elem)
    
class SimpleSubsetsTest(unittest.TestCase):
    def setUp(self):
        self.its_set = set([1, 2, 3])
    
    def test_simple_subsets(self):
        expected = [set([]),
                    set([1]), set([2]), set([3]),
                    set([1, 2]), set([1, 3]), set([2, 3]),
                    set([1, 2, 3])]
        actual = []
        for subset in subset_generator(self.its_set):
            actual.append(subset)
        self.assertListEqual(expected, actual)
        self.assertEquals(len(expected), len(actual))
                                                         
if __name__ == '__main__':
    unittest.main()
