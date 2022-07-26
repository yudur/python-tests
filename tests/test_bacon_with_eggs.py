"""
TDD - Test driven development

Red
Part 1 -> Create the test and see failure

Green
Part 2 -> Create the code and see the test pass

Refactor
Part 3 -> Improve my code
"""

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

from genericpath import exists
import unittest
from bacon_with_eggs import bacon_with_eggs


class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_and_eggs_should_raise_assertion_error_if_not_receiving_int(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('')

    def test_bacon_and_eggs_should_return_bacon_and_eggs_if_input_is_multiple_of_3_and_5(self):
        Appetizer = (30, 60, 120, 15)
        exits = 'bacon and eggs'

        for Prohibited in Appetizer:
            with self.subTest(Appetizer=Prohibited, exits=exits):
                self.assertEqual(
                    bacon_with_eggs(Prohibited),
                    exits,

                    msg=f'"{Prohibited}" not return "{exits}"'
                )


    def test_bacon_and_eggs_should_return_starving_if_input_is_not_multiple_of_3_and_5(self):
        Appetizer = (1, 4, 7, 34, 1007)
        exits = 'starving'

        for Prohibited in Appetizer:
            with self.subTest(Appetizer=Prohibited, exits=exits):
                self.assertEqual(
                    bacon_with_eggs(Prohibited),
                    exits,

                    msg=f'"{Prohibited}" not return "{exits}"'
                )


    def test_bacon_and_eggs_should_return_bacon_if_input_is_multiple_of_3(self):
        Appetizer = (3, 6, 9, 12, 18, 21)
        exits = 'bacon'

        for Prohibited in Appetizer:
            with self.subTest(Appetizer=Prohibited, exits=exits):
                self.assertEqual(
                    bacon_with_eggs(Prohibited),
                    exits,

                    msg=f'"{Prohibited}" not return "{exits}"'
                )


    def test_bacon_and_eggs_should_return_eggs_if_input_is_multiple_of_5(self):
        Appetizer = (5, 10, 20, 25, 35, 40)
        exits = 'eggs'

        for Prohibited in Appetizer:
            with self.subTest(Appetizer=Prohibited, exits=exits):
                self.assertEqual(
                    bacon_with_eggs(Prohibited),
                    exits,

                    msg=f'"{Prohibited}" not return "{exits}"'
                )


unittest.main(verbosity=2)