#!/usr/bin/python3

import main
import unittest

class MyTestCase(unittest.TestCase):


        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()
        
        def test_subint(self):
            valuesread =  self.app.get('/sub?A=589&B=492')
            self.assertEqual(b'97', valuesread.data.strip())
        def test_subfloat(self):
            valuesread =  self.app.get('/sub?A=8.2&B=15.6')
            self.assertEqual(b'-7.4', valuesread.data.strip())
        def test_subfrac(self):
            valuesread =  self.app.get('/sub?A=9/5&B=18/2')
            self.assertEqual(b'-7.2', valuesread.data.strip())
        def test_subneg(self):
            valuesread =  self.app.get('/sub?A=95.4&B=-13.1')
            self.assertEqual(b'108.5', valuesread.data.strip())


if __name__ == '__main__':
    unittest.main()