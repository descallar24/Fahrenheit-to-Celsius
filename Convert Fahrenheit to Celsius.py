import unittest

def f_to_c(f):
    c = (5/9) * (f - 32)
    return c

class FahrenheitToCelsiusTest(unittest.TestCase):
    def test_positive_temperature(self):
        f = 68  # Example Fahrenheit temperature
        expected_c = 20  # Expected Celsius temperature
        result_c = f_to_c(f)
        self.assertEqual(result_c, expected_c)

    def test_negative_temperature(self):
        f = -40  # Example Fahrenheit temperature
        expected_c = -40  # Expected Celsius temperature
        result_c = f_to_c(f)
        self.assertEqual(result_c, expected_c)

    def test_zero_temperature(self):
        f = 32  # Example Fahrenheit temperature
        expected_c = 0  # Expected Celsius temperature
        result_c = f_to_c(f)
        self.assertEqual(result_c, expected_c)

if __name__ == '__main__':
    unittest.main()
