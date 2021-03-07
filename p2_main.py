import unittest
import p2_leap

class FizzBuzzTest(unittest.TestCase):
  def test_fizzBuzz1(self):
    self.assertEqual(self.test_case(), p2_leap.output(400))

  def test_case(self):
    return True
if __name__ == '__main__':
    unittest.main()