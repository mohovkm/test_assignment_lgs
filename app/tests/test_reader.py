import unittest
from classes import CSVFileReader, NotAValidFileException
from datetime import datetime
from decimal import Decimal


class TestReader(unittest.TestCase):
    def test_wrong_input_path_error(self):
        """Raises an error, when wrong type of path given.

        :return:
        """
        with self.assertRaises(NotAValidFileException):
            CSVFileReader(123)

    def test_not_existed_path(self):
        """Returns an empty list, when given not existed path.

        :return:
        """
        self.assertEqual([], CSVFileReader('vasya').read())

    def test_read_right(self):
        """Read csv file and returns List[List[dict]]

        :return:
        """
        to_compare = [[
            {
                'date': datetime(2019, 10, 1, 0, 0),
                'type': 'remove',
                'amount': Decimal('99.20'),
                'from': 198,
                'to': 182
            },
            {
                'date': datetime(2019, 10, 2, 0, 0),
                'type': 'add',
                'amount': Decimal('2000.10'),
                'from': 188,
                'to': 198
            }
        ]]

        self.assertEqual(to_compare, CSVFileReader('tests/bank1.csv').read())
