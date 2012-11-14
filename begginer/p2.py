"""Problem 2"""

import unittest

def merge(first, second):
    """
    Merges two objects with any depth(of all types).
    0. Type mismatches will yield a tuple with the two elements
    1. Numbers are to be added
    2. Strings are to be appended
    3. Lists are to be appended
    4. Sets are to be unioned
    5. dicts are to be updated
    """
    firsts_type = type(first)
    seconds_type = type(second)

    if firsts_type != seconds_type:
        return (first, second)
    if firsts_type is dict:
        return merge_dicts(first, second)
    elif firsts_type is set:
        return first | second
    else:
        return first + second


def merge_dicts(first, second):
    """ """
    first_keys = first.keys()
    second_keys = second.keys()
    third = {}
    for key in set(first_keys) | set(second_keys):
        third[key] = merge(first[key], second[key])
    return third

class MergeDictsTest(unittest.TestCase):
    def setUp(self):
        self.first = {
            'x' : [1, 2, 3],
            'y' : 1,
            'z' : set([1, 2, 3]),
            'w' : 'qweqwe',
            't' : {
                'a' : [1, 2]
                },
            'm' : [1]
            }
        self.second = {
            'x' : [4, 5, 6],
            'y' : 4,
            'z' : set([4, 2, 3]),
            'w' : 'asdf',
            't' : {
                'a' : [3, 2]
                },
            'm' : 'wer'
            }
    def test_merge_dicts(self):
        self.expected = {
            'x' : [1, 2, 3, 4, 5, 6],
            'y' : 5,
            'z' : set([1, 2, 3, 4]),
            'w' : 'qweqweasdf',
            't' : {
                'a' : [1, 2, 3, 2]
                },
            'm' : ([1], 'wer')
            }
        self.actual = merge(self.first, self.second)
        self.assertDictEqual(self.expected, self.actual)

class MergeMismatchedTest(unittest.TestCase):
    def setUp(self):
        self.first = [1, 2, 3]
        self.second = 'banana'
        
    def test_merge_mismatched(self):
        self.expected = (self.first, self.second)
        self.actual = merge(self.first, self.second)
        self.assertEquals(self.expected, self.actual)

class MergeIntegersTest(unittest.TestCase):
    def setUp(self):
        self.first = 1
        self.second = 42

    def test_merge_integers(self):
        self.expected = self.first + self.second
        self.actual = merge(self.first, self.second)
        self.assertEquals(self.expected, self.actual)

class MergeFloatsTest(unittest.TestCase):
    def setUp(self):
        self.first = 1.0
        self.second = 3.14

    def test_merge_floats(self):
        self.expected = self.first + self.second
        self.actual = merge(self.first, self.second)
        self.assertAlmostEqual(self.expected, self.actual, 0.01)

class MergeListTest(unittest.TestCase):
    def setUp(self):
        self.first = [1, 2, 3]
        self.second = [9, 8, 10]
    
    def test_merge_lists(self):
        self.expected = self.first + self.second
        self.actual = merge(self.first, self.second)
        self.assertListEqual(self.expected, self.actual)

class MergeStringsTest(unittest.TestCase):
    def setUp(self):
        self.first = 'foo'
        self.second = 'bar'

    def test_merge_strings(self):
        self.expected = self.first + self.second
        self.actual = merge(self.first, self.second)
        self.assertEquals(self.expected, self.actual)

class MergeSetsTest(unittest.TestCase):
    def setUp(self):
        self.first = set([1, 2, 3])
        self.second = set([2, 3, 4])

    def test_merge_sets(self):
        self.expected = self.first | self.second
        self.actual = merge(self.first, self.second)
        self.assertSetEqual(self.expected, self.actual)


if __name__ == '__main__':
    unittest.main()
