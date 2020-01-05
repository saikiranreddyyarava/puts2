import main
import unittest

class MyTestCase(unittest.TestCase):

	def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

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

if __name__ == '__main__':
    unittest.main()
