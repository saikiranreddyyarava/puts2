#!/usr/bin/python3

import main
import unittest

class MyTestCase(unittest.TestCase):


        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_addint(self):
            valuesread=  self.app.get('/add?A=9&B=69')
            self.assertEqual(b'78', valuesread.data.strip())
        def test_addfloat(self):
            valuesread=  self.app.get('/add?A=9.2&B=6.4')
            self.assertEqual(b'15.6', valuesread.data.strip())
        def test_addfrac(self):
            valuesread =  self.app.get('/add?A=5/2&B=9/4')
            self.assertEqual(b'4.75', valuesread.data.strip())
        def test_addneg(self):
            valuesread=  self.app.get('/add?A=15.1&B=-8.2')
            self.assertEqual(b'6.9', valuesread.data.strip())

if __name__ == '__main__':
    unittest.main()
