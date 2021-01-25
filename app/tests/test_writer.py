import unittest
from classes import CSVFileWriter, CSVFileWriterTypeError


class TestWriter(unittest.TestCase):
    def test_wrong_input_path_error(self):
        """Raises an error, when wrong type of path given.

        :return:
        """
        with self.assertRaises(CSVFileWriterTypeError):
            CSVFileWriter(123)
