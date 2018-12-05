#!/usr/bin/python
"""
Created on Mon Dec  3 11:41:52 2018

@author: dcdit
"""

import unittest
from exponent import exponent

class TestExponent(unittest.TestCase):
    def test_square_of_two(self):
        self.assertEqual(exponent.exp(2,2), 4)

    def test_square_of_negative_two(self):
        self.assertEqual(exponent.exp(-2,2),4)

    def test_two_pow_negative_two(self):
        self.assertEqual(exponent.exp(2,-2),0.25)

    def test_two_pow_zero(self):
        self.assertEqual(exponent.exp(2,0),1)

    def test_zero_pow_zero(self):
        self.assertEqual(exponent.exp(0,0),"(undefined)")

if __name__ == "__main__":
    unittest.main()
