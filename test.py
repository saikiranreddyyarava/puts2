import main
import unittest

class MyTestCase(unittest.TestCase):

	def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

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

if __name__ == '__main__':
    unittest.main()
