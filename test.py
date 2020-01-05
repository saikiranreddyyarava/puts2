import main
import unittest

class MyTestCase(unittest.TestCase):

<<<<<<< HEAD
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
=======
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
>>>>>>> subtraction

if __name__ == '__main__':
    unittest.main()
