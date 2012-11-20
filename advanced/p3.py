"""
Problem 3
"""

import unittest

class Highlander(type):
    """There can be only one"""
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Highlander, cls).__new__(cls, 
                                                           *args, 
                                                           **kwargs)
        return cls._instance
    
class MacLeod(object):
    pass

class SingletonTest(unittest.TestCase):
    def setUp(self):
        self.duncan = Highlander(MacLeod)
        self.connor = Highlander(MacLeod)

    def test_singleton(self):
        self.assertEquals(self.duncan, self.connor)

if __name__ == '__main__':
    unittest.main()
