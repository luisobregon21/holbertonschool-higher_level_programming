#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    ''' Class tests max integer function'''
    def test_max(self):
        ''' Tests for regular max in list '''
        l = [1, 2, 3, 4]
        self.assertEqual(max_integer(l), 4)

        l = [1, 2, 4, 8]
        self.assertEqual(max_integer(l), 8)

        l = [1, 22, 3, 4]
        self.assertEqual(max_integer(l), 22)

        l = [1, 2, 3.5, 4]
        self.assertEqual(max_integer(l), 4)

        l = [-5, -2, 8, -7]
        self.assertEqual(max_integer(l), 8)

        l = [None]
        self.assertEqual(max_integer(l), None)

        l = [100, 2, 3, 4]
        self.assertEqual(max_integer(l), 100)

        l = [6, 2, 3, 14, 8, 9, 7]
        self.assertEqual(max_integer(l), 14)

        l = [-1, -2, -3, -4]
        self.assertEqual(max_integer(l), -1)

        l = [3]
        self.assertEqual(max_integer(l), 3)

        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
