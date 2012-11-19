"""
Problem 2
Write a generator that returns all the subsets of a given set.
"""

import unittest

class Subsets(object):
    def __init__(self, its_set):
        self.its_set = its_set

    def __iter__(self):
        ## iterate somehow
        inititial_set_size = len(self.its_set)
        for set_size in range(inititial_set_size+1):
            partial = set([])
            for elem in self.its_set:
                if len(partial) == set_size:
                    yield partial
                    break
                else:
                    partial |= set([elem])

class SimpleSubsetsTest(unittest.TestCase):
    def setUp(self):
        self.subsets = Subsets(set([1, 2, 3]))
    
    def test_simple_subsets(self):
        expected = [set([1, 2, 3]),
                    set([1, 2]),
                    set([1, 3]),
                    set([2, 3]),
                    set([1]),
                    set([2]),
                    set([3]),
                    set([])]
        actual = []
        for subset in self.subsets:
            actual.append(subset)
        self.assertEquals(len(expected), len(actual))
        self.assertListEqual(expected, actual)
                                                         
if __name__ == '__main__':
    unittest.main()
