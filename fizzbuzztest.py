import fizzbuzz
import unittest

class testfb(unittest.TestCase):

    def test_printnumbers(self):
        for x in range(1, 101):
            if x % 3 != 0 or x % 5 != 0:
                self.assertEqual(fizzbuzz.fb(x), x)


if __name__ == "__main__":
    unittest.main()
