"""Problem 1"""

import unittest

def flatten(list_a, list_b, max_depth):
    """
    Implements a function that flattens two lists up to a 
    maximum given depth
    """
    first = flatten_again(list_a, max_depth)
    second = flatten_again(list_b, max_depth)
    return first + second

def flatten_again(collection, depth):
    """
    Returns the flattened list upto a depth
    """
    collection_is_not_iterable = not hasattr(collection, '__contains__')
    depth_reached = depth==0
    if depth_reached or collection_is_not_iterable:
        return [collection]
    x = []
    for entry in collection:
        flattened = flatten_again(entry, depth-1)
        x = x + flattened
    return x

class FlettenWithDepthOneTest(unittest.TestCase):
    """As simple as possible"""
    def setUp(self):
        self.list_a = [1, 2, 3, 4]
        self.list_b = [2, 3, 4, 5, 123]
    
    def test_flatten_depth_one(self):
        self.expected = self.list_a + self.list_b
        self.actual = flatten(self.list_a, self.list_b, 1)
        self.assertListEqual(self.expected, self.actual)

class FlattenWithDepthTwoTest(unittest.TestCase):
    """List has depth of three, maxdepth is two"""
    def setUp(self):
        self.list_a = [1, 2, [3, 4]]
        self.list_b = [2, [[3, 4, 5], 6]]

    def test_flatten_depth_two(self):
        self.expected = [1, 2, 3, 4, 2, [3, 4, 5], 6]
        self.actual = flatten(self.list_a, self.list_b, 2)
        self.assertListEqual(self.expected, self.actual)

class FlattenWithDepthThreeTest(unittest.TestCase):
    """List has depth of three, maxdepth is three"""
    def setUp(self):
        self.list_a = [1, 2, [3, 4]]
        self.list_b = [2, [[3, 4, 5], 6]]

    def test_flatten_depth_three(self):
        self.expected = [1, 2, 3, 4, 2, 3, 4, 5, 6]
        self.actual = flatten(self.list_a, self.list_b, 3)
        self.assertListEqual(self.expected, self.actual)


if __name__ == '__main__':
    unittest.main()
