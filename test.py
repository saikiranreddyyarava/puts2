import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

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
