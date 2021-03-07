import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
  def test_fizzBuzz1(self):
    self.assertEqual(self.test_case(), fizzbuzz.output(1, 12))

  def test_case(self):
    return '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\n'

if __name__ == '__main__':
    unittest.main()