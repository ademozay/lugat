import unittest

from lugat import lookup, LookupException

class TestLugat(unittest.TestCase):

    def test_lookup(self):
        word        = lookup('ipek')
        variations  = word.get_variations()
        self.assertNotEqual(len(variations), 0)
