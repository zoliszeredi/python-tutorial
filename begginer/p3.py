"""Problem 3"""

import unittest
import sys

def read_dict_list_from(filename = None):
    """
    Reads a list of dictionaries read from a file or stdin.
    Returns:
    The dict list
    Input Format:
    <key> <value>
    Ex:
    'f' 1 
    'b' 44
    'c' 3

    'n' 4
    's' 7 
    """
    if filename is None:
        stream = sys.stdin
        its_lines = stream.readlines()
    else:
        stream = open(filename, 'r')
        its_lines = stream.readlines()
        stream.close()
    its_list = []
    its_dict = {}
    for line in its_lines:
        if len(line)>1:
            key, value = line.split(' ')    
            its_dict[key] = int(value)
        else:
            its_list.append(dict(its_dict))
            its_dict = {}
    return its_list

def write_dict_list_to(its_list, filename = None):
    """
    Writes a list of dictionaries to a filename or stdout.
    """
    if filename is None:
        stream = sys.stdin
    else:   
        stream = open(filename, 'w')

    for its_dict in its_list:
        stream.write(repr(its_dict))
    stream.write('\n')

    if filename is not None:
        stream.close()

def sort_dict_list(its_list):
    """
    Implements dictionary list sorting algorithm, with quicksort.
    
    """
    its_length = len(its_list)
    if its_length <= 1:
        return its_list
    pivot = its_list[its_length/2]
    its_list.remove(pivot)
    lesser = []
    greater = []
    for entry in its_list:
        if compare_dicts(entry, pivot)<0:
            lesser.append(entry)
        else:
            greater.append(entry)
    return sort_dict_list(lesser) + [pivot] + sort_dict_list(greater)

def compare_dicts(first, second):
    """
    Rules:
    first < second, if
        first[key1] < second[key2], else
        del first[key1], second[key2]
        key1, key2 = min(first.keys()), min(second.keys())

    Returns:
    <0 : first < second 
    =0 : first == second
    >0 : first > second 
    """
    remainder_keys = first.keys()
    not_done = True
    while not_done:
        firsts_min = min(remainder_keys)
        if firsts_min in second.keys():
            diff = first[firsts_min] - second[firsts_min]
            if diff != 0:
                return diff
            else:
                remainder_keys.remove(firsts_min) 
        else:
            seconds_min = min(second.keys())
            diff = ord(firsts_min)-ord(seconds_min)
            return diff
        not_done = len(remainder_keys) > 0
    return 0

class CompareSimpleDictsTest(unittest.TestCase):
    def setUp(self):
        self.first = {
            'b' : 2,
        }
        self.second = {
            'a' : 1,
        }
    def test_compare_simple_dicts(self):
        self.result = compare_dicts(self.first, self.second)
        self.assertTrue(self.result > 0)

class CompareSameKeysDictsTest(unittest.TestCase):
    def setUp(self):
        self.first = { 'b' : 2, 'c' : 3 }
        self.second = { 'b' : 3 }

    def test_dict_same_smallest_key(self):
        self.result = compare_dicts(self.first, self.second)
        self.assertTrue(self.result < 0)

class CompareSameDictsTest(unittest.TestCase):
    def setUp(self):
        self.first = { 'b' : 2, 'c' : 3 }
        self.second = { 'b' : 2, 'c' : 3 }

    def test_dict_same(self):
        self.result = compare_dicts(self.first, self.second)
        self.assertTrue(self.result == 0)

class SortDictTest(unittest.TestCase):
    def setUp(self):
        self.its_list = [
            { 'a' : 4, 'b' : 2, 'c' : 3 },
            { 'a' : 2 },
            { 't' : 10 },
            { 'b' : 4, 'c' : 2, 'd' : 3 }
            ]
    def test_sort(self):
        self.expected = [
            { 'a' : 2 },
            { 'a' : 4, 'b' : 2, 'c' : 3 },
            { 'b' : 4, 'c' : 2, 'd' : 3 },
            { 't' : 10 }
            ]
        self.actual = sort_dict_list(self.its_list)
        self.assertListEqual(self.expected, self.actual)

def test_all():
    its_list = read_dict_list_from('dict.in')
    write_dict_list_to(sort_dict_list(its_list), 'dict.out')

if __name__ == '__main__':
    test_all()
    unittest.main()

