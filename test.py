import main
import unittest

class MyTestCase(unittest.TestCase):


        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_addint(self):
            valuesread=  self.app.get('/add?A=4&B=9')
            self.assertEqual(b'13.0', valuesread.data)
        def test_addfloat(self):
            valuesread=  self.app.get('/add?A=4.2&B=6.4')
            self.assertEqual(b'10.6', valuesread.data)
        def test_addfrac(self):
            valuesread =  self.app.get('/add?A=6/2&B=8/3')
            self.assertEqual(b'5.667', valuesread.data)
        def test_addneg(self):
            valuesread=  self.app.get('/add?A=6.2&B=-8.2')
            self.assertEqual(b'-2.0', valuesread.data)

	def test_subint(self):
            valuesread =  self.app.get('/sub?A=9&B=13')
            self.assertEqual(b'-4.0', valuesread.data)
        def test_subfloat(self):
            valuesread =  self.app.get('/sub?A=4.3&B=9.8')
            self.assertEqual(b'-5.5', valuesread.data)
        def test_subfrac(self):
            valuesread =  self.app.get('/sub?A=8/3&B=9/2')
            self.assertEqual(b'-1.833', valuesread.data)
        def test_subneg(self):
            valuesread =  self.app.get('/sub?A=6.4&B=-9.3')
            self.assertEqual(b'2.9', valuesread.data)


	def test_mulint(self):
            valuesread =  self.app.get('/mul?A=12&B=10')
            self.assertEqual(b'120.0', valuesread.data)
        def test_mulfloat(self):
            valuesread =  self.app.get('/mul?A=6.2&B=8.4')
            self.assertEqual(b'52.08', valuesread.data)
        def test_mulfrac(self):
            valuesread =  self.app.get('/mul?A=6/2&B=7/5')
            self.assertEqual(b'4.2', valuesread.data)
        def test_mulneg(self):
            valuesread =  self.app.get('/mul?A=7.5&B=-9.3')
            self.assertEqual(b'-69.75', valuesread.data)


 	def test_divint(self):
            valuesread =  self.app.get('/div?A=6&B=9')
            self.assertEqual(b'0.667', valuesread.data)
        def test_divfloat(self):
            valuesread =  self.app.get('/div?A=6.4&B=5.5')
            self.assertEqual(b'1.164', valuesread.data)
        def test_divfrac(self):
            valuesread =  self.app.get('/div?A=6/4&B=9/5')
            self.assertEqual(b'0.833', valuesread.data)
        def test_divneg(self):
            valuesread =  self.app.get('/div?A=6.5&B=-9.8')
            self.assertEqual(b'-0.663', valuesread.data)
        def test_zerodiv(self):
            valuesread = self.app.get('/div?A=6&B=9/0')
            self.assertEqual(b'None',valuesread.data)


if __name__ == '__main__':
    unittest.main()
