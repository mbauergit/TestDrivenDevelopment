import leapyear
import unittest

class testly(unittest.TestCase):

    def test_divby4(self):
        self.assertEqual(leapyear.ly(4), "Is a leap year")
        self.assertEqual(leapyear.ly(2024), "Is a leap year")

if __name__ == "__main__":
    unittest.main()
