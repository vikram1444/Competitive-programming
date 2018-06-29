import unittest

fibs = {0: 0, 1: 1}

def fibonacci(n):
    if n <= 0:
        return 0

    if n in fibs:
        return fibs[n]

    fibs[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibs[n]
# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fibonacci(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fibonacci(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fibonacci(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fibonacci(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fibonacci(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fibonacci(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)
