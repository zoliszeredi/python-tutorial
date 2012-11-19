"""
Problem 1
Given a binary tree as a tuple (label, left, right) write an iterator/generator 
for pre-order traversal
"""
import unittest

class BinaryTree(object):
    """
    Generator for traversing a binary tree
    """
    def __init__(self, node):
        self.root = node
    
    def pre_order(self, node):
        """Label, left, right"""
        if node:
            label, left, right = node
            yield label
            for label in self.pre_order(left):
                yield label
            for label in self.pre_order(right):
                yield label

    def left(self):
        """Left branch"""
        return self.root[1]

    def right(self):
        """Right branch"""
        return self.root[2]

    def __iter__(self):
        return self.pre_order(self.root)
    
class SimpleTreeTest(unittest.TestCase):
    """
    Tests the traversal of a binary Tree with a few nodes
    """
    def setUp(self):
        self.node = (('b', 
                      ('a', None, None), 
                      ('z', 
                       ('c', None, None), 
                       ('zz', None, None))))
        self.root = BinaryTree(self.node)

    def test_simple_iter(self):
        """Simple traversal test"""
        expected_labels = ['b', 'a', 'z', 'c', 'zz']
        actual_labels = []
        for node in self.root:
            actual_labels.append(node)
        self.assertListEqual(expected_labels, actual_labels)

class LargerTreeTest(unittest.TestCase):
    """
    Tests the traversal of a binary Tree with many nodes
    """
    def setUp(self):
        self.node = ('x', 
                     ('f', 
                      ('e', 
                       ('q', 
                        ('p', None, None),
                        None),
                       ('o', None, None)),
                      ('d', 
                       ('r', 
                        ('n', None, None),
                        ('m', None, None)),
                       None)),
                     ('z', 
                      ('a', 
                       ('w', None, None),
                       ('h', None, None)),
                      ('y', 
                       None, 
                       ('c', None,  None))))
        self.root = BinaryTree(self.node)

    def test_larger_iter(self):
        """Larger traversal test"""
        expected_labels = ['x', 'f', 'e', 'q', 'p', 'o', 'd', 'r', 
                           'n', 'm', 'z', 'a', 'w', 'h', 'y', 'c']
        actual_labels = []
        for node in self.root:
            actual_labels.append(node)
        self.assertListEqual(expected_labels, actual_labels)

class EmptyTreeTest(unittest.TestCase):
    """
    Test the traversal of an empty Tree
    """
    def setUp(self):
        self.node = (None, None, None)
        self.root = BinaryTree(self.node)

    def test_empty(self):
        """Empty tree test"""
        expected = [None]
        actual = []
        for node in self.root:
            actual.append(node)
        self.assertListEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

