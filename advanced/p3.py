"""
Problem 3
"""

import unittest

class Highlander(type):
    """There can be only one"""
    def __init__(metaclass, name, bases, dictionary):
        super(Highlander, metaclass).__init__(name,
                                              bases,
                                              dictionary)
        metaclass.instance = None

    def __call__(metaclass, *args, **kwargs):
        if metaclass.instance is None:
            metaclass.instance = super(Highlander, 
                                       metaclass).__call__(*args, 
                                                            **kwargs)
        return metaclass.instance
    
class MacLeod(object):
    __metaclass__ = Highlander
    def method(self):
        print "i am of the MacLeod clan"

class Kell(object):
    __metaclass__ = Highlander
    def method(self):
        print "i am of the Kell clan"

class SingletonTest(unittest.TestCase):
    def setUp(self):
        self.duncan = MacLeod()
        self.connor = MacLeod()
        self.jacob = Kell()

    def test_first_type(self):
        self.assertEquals(self.duncan, self.connor)

    def test_second_type(self):
        self.assertNotEqual(self.duncan, self.jacob)

if __name__ == '__main__':
    unittest.main()
