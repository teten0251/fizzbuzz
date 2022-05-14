import unittest
from fizzbuzz import Fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):
    def test_outputFizzBuzz(self):
        self.assertEqual(Fizzbuzz.calculate(90), 'fizzbuzz')

    def test_outputFizz(self):
        self.assertEqual(Fizzbuzz.calculate(99), 'fizz')

    def test_outputBuzz(self):
        self.assertEqual(Fizzbuzz.calculate(80), 'buzz')


if __name__ == '__main__':
    unittest.main()
