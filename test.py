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

        def test_subint(self):
            valuesread =  self.app.get('/sub?A=9&B=13')
            self.assertEqual(b'-4.0', valuesread.data.strip())
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



        def test_mulint(self):
            valuesread =  self.app.get('/mul?A=12&B=10')
            self.assertEqual(b'120.0', valuesread.data.strip())       
        def test_mulint(self):
            valuesread =  self.app.get('/mul?A=123&B=298')
            self.assertEqual(b'36654', valuesread.data.strip())
        def test_mulfloat(self):
            valuesread =  self.app.get('/mul?A=6.2&B=8.6')
            self.assertEqual(b'53.32', valuesread.data.strip())
        def test_mulfrac(self):
            valuesread =  self.app.get('/mul?A=6/2&B=7/5')
            self.assertEqual(b'4.2', valuesread.data.strip())
        def test_mulneg(self):
            valuesread =  self.app.get('/mul?A=7.5&B=-9.3')
            self.assertEqual(b'-69.75', valuesread.data.strip())

        def test_divint(self):
            valuesread =  self.app.get('/div?A=6&B=15')
            self.assertEqual(b'0.4', valuesread.data.strip())
        def test_divfloat(self):
            valuesread =  self.app.get('/div?A=6.4&B=3.2')
            self.assertEqual(b'2.0', valuesread.data.strip())
        def test_divfrac(self):
            valuesread =  self.app.get('/div?A=18/5&B=24/2')
            self.assertEqual(b'0.075', valuesread.data.strip())
        def test_divneg(self):
            valuesread =  self.app.get('/div?A=16.1&B=-5/2')
            self.assertEqual(b'-1.61', valuesread.data.strip())
        def test_zerodiv(self):
            valuesread = self.app.get('/div?A=16.1&B=5/0')
            self.assertEqual(b'"ERROR! invalid input"',valuesread.data.strip())


if __name__ == '__main__':
    unittest.main()
