"""Problem 1"""

import unittest

def swap_keys_with_vals(its_dict):
    """
    Swaps the dictionaries keys with it's values if possible,
    otherwise print 'Swap is not possible'
    """
    impossible_message = 'Swap is not possible'
    result = {}
    unhashables = (type(()), type([]), type(set()), type({}))
    for key, value in its_dict.iteritems():
        if type(value) in unhashables:
            return impossible_message
        else:
            result[value] = key
    return result

class SimpleSwapDictKeysTest(unittest.TestCase):
    """Trivial key, value swap"""
    def setUp(self):
        self.its_dict = { 'a' : 123, 'b' : 456 }

    def test_simple_swap(self):
        """Swap test"""
        expected = { 123 : 'a', 456 : 'b' }
        actual = swap_keys_with_vals(self.its_dict)
        self.assertDictEqual(expected, actual)

# class AdvancedSwapDictKeysTest(unittest.TestCase):
#     def setUp(self):
#         self.its_dict = { }

#     def test_advanced_swap(self):
#         pass

class ImpossibleDictSwapTest(unittest.TestCase):
    def setUp(self):
        self.its_dict_with_tuple = { 'a' : (1, 2, [3]) }
        self.its_dict_with_set = { 'a' : set([1, 2, 3]) }
        self.its_dict_with_list = { 'a' : [1, 2, [3]] }

    def test_impossible_set_swap(self):
        expected = 'Swap is not possible'
        actual = swap_keys_with_vals(self.its_dict_with_set)
        self.assertEquals(expected, actual)

    def test_impossible_tuple_swap(self):
        expected = 'Swap is not possible'
        actual = swap_keys_with_vals(self.its_dict_with_tuple)
        self.assertEquals(expected, actual)

    def test_impossible_list_swap(self):
        expected = 'Swap is not possible'
        actual = swap_keys_with_vals(self.its_dict_with_list)
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()

