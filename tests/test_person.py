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
from unittest.mock import patch
from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('Yudi', 'Duarte')
        self.p2 = Person('Aninha', 'Silva')

    def test_person_attr_name_has_the_correct_value(self):
        self.assertEqual(self.p1.first_name, 'Yudi')

        self.assertEqual(self.p2.first_name, 'Aninha')

    def test_person_attr_name_is_str(self):
        self.assertIsInstance(self.p1.first_name, str)

        self.assertIsInstance(self.p2.first_name, str)

    def test_person_attr_last_name_has_the_correct_value(self):
        self.assertEqual(self.p1.last_name, 'Duarte')

        self.assertEqual(self.p2.last_name, 'Silva')

    def test_person_attr_last_name_is_str(self):
        self.assertIsInstance(self.p1.last_name, str)

        self.assertIsInstance(self.p2.last_name, str)

    def test_person_attr_data_obtained_starts_false(self):
        self.assertFalse(self.p1.data_obtained)
        
        self.assertFalse(self.p2.data_obtained)

    def test_get_all_successful_data_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p2.data_obtained)

    def test_get_all_data_failure_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'ERRO 404')
            self.assertFalse(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'ERRO 404')
            self.assertFalse(self.p2.data_obtained)

    def test_get_all_data_sequential_success_and_failure(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p2.data_obtained)
            
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'ERRO 404')
            self.assertFalse(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'ERRO 404')
            self.assertFalse(self.p2.data_obtained)


if __name__ == '__main__':
    unittest.main(verbosity=2)
