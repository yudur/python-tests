try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    # calculator soma function:   soma(x -> (int, float), y -> (int, float)) -> (int, float)

    def test_adds_5_and_5_should_return_10(self):
        self.assertEqual(calculator.soma(5, 5), 10)

    def test_sums_negative_5_and_5_should_return_0(self):
        self.assertEqual(calculator.soma(-5, 5), 0)

    def test_soma_several_entries(self):
        x_y_outputs = (
            (10, 10, 20),
            (5, 5, 10),
            (-145, 10, -135),
            (2.6, 2.4, 5),
            (100, 150.9, 250.9),
        )

        for x_y_outputs in x_y_outputs:
            with self.subTest(x_y_outputs=x_y_outputs):
                x, y, output = x_y_outputs
                self.assertEqual(calculator.soma(x, y), output)

    def test_sum_x_is_not_int_or_float_should_return_assertonerror(self):
        with self.assertRaises(AssertionError):
            calculator.soma('11', 1)

    def test_sum_y_is_not_int_or_float_should_return_assertonerror(self):
        with self.assertRaises(AssertionError):
            calculator.soma(11, '1')

    # calculator subtrai function:    soma(x -> (int, float), y -> (int, float)) -> (int, float)

    def test_subtract_12_and_6_should_return_6(self):
        self.assertEqual(calculator.subtrai(12, 6), 6)

    def test_subtract_negative_50_and_5_should_return_0(self):
        self.assertEqual(calculator.soma(-50, 5), -45)

    def test_subtrai_several_entries(self):
        x_y_outputs = (
            (-10, 10, -20),
            (500, 5, 495),
            (-145, 10, -155),
            (2.6, 2.4, 0.20000000000000018),
            (-100, -150.9, 50.900000000000006),
        )

        for x_y_outputs in x_y_outputs:
            with self.subTest(x_y_outputs=x_y_outputs):
                x, y, output = x_y_outputs
                self.assertEqual(calculator.subtrai(x, y), output)

    def test_subtrai_x_is_not_int_or_float_should_return_assertonerror(self):
        with self.assertRaises(AssertionError):
            calculator.soma('10', 100)

    def test_subtrai_y_is_not_int_or_float_should_return_assertonerror(self):
        with self.assertRaises(AssertionError):
            calculator.soma(10, '100')

unittest.main(verbosity=2)
