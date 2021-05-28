import leapyear
import unittest

class testly(unittest.TestCase):

    def test_divby4(self):
        self.assertEqual(leapyear.ly(4), "Is a leap year")
        self.assertEqual(leapyear.ly(2024), "Is a leap year")
        self.assertEqual(leapyear.ly(1999), "Is not a leap year")

    def test_divby100(self):
        self.assertEqual(leapyear.ly(2100), "Is not a leap year")
        self.assertEqual(leapyear.ly(1900), "Is not a leap year")

    def test_divby400(self):
        self.assertEqual(leapyear.ly(2000), "Is a leap year")
        self.assertEqual(leapyear.ly(2400), "Is a leap year")

if __name__ == "__main__":
    unittest.main()
