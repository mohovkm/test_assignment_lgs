import csv
import logging
from abc import ABC, abstractmethod
from typing import List, Union
from pathlib import Path
from decimal import Decimal
from .parser import Parser


class CSVReaderException(Exception):
    pass


class NotAFileException(CSVReaderException):
    pass


class NotAValidFileException(CSVReaderException):
    pass


class Reader(ABC):
    @abstractmethod
    def read(self) -> List[List[dict]]:
        pass


class CSVFileReader(Reader):
    _mapping = {
        'date': {
            'aliases': ['timestamp', 'date', 'date_readable'],
            'func': lambda x: Parser.parse_data(x, ['%d-%m-%Y', '%d %b %Y', '%b %d %Y'])
        },
        'type': {
            'aliases': ['transaction', 'type'],
            'func': lambda x: str(x)
        },
        'amount': {
            'aliases': ['amount', 'amounts', 'euro', 'cents'],
            'func': lambda x: Decimal(x),
            'concat': ['euro', 'cents']
        },
        'from': {
            'aliases': ['from'],
            'func': lambda x: int(x)
        },
        'to': {
            'aliases': ['to'],
            'func': lambda x: int(x)
        },
    }

    def __init__(self, files: List[Union[str, Path]]):
        """Initialisation.

        :param files: (List[Union[str, Path]) - list with paths to files to read.
        """
        if isinstance(files, str) or isinstance(files, Path):
            files = [files]

        if not isinstance(files, list):
            detail = f'Files must an instance of [list, str, Path] got [{type(files)}] instead.'
            raise NotAValidFileException(detail)

        self.files = files

    def read(self) -> List[List[dict]]:
        """Reader implementation.
        Method uses csv.DictReader to read csv files and returns List[List[dict]], where:
        List[ - main container for all files
            List[ - csv file
                dict - csv file content
            ]
        ]

        :return: List[List[dict]]
        """
        result = []

        for path in self.files:
            path = Path(path)
            if not path.is_file():
                detail = f'File is not exist: [{path}]'
                logging.error(detail)
                continue

            with open(path, mode='r') as f:
                csv_reader = csv.DictReader(f)
                csv_data = []

                for row in csv_reader:
                    obj = {}

                    # In each row we are trying to find alias and parse value to right format
                    for key, value in self._mapping.items():
                        val = None
                        aliases = [x for x in value.get('aliases', []) if x in row]
                        if len(aliases) == 0:
                            continue

                        # If we have "concat" in a mapping, then we need to concat values before transformation
                        if len(aliases) > 1 and value.get('concat', False):
                            values_to_concat = []
                            for alias in value.get('concat', []):
                                values_to_concat.append(row[alias])
                            val = '.'.join(values_to_concat)

                        if val is None:
                            alias = aliases[0]
                            val = value.get('func', lambda x: x)(row[alias])
                        else:
                            val = value.get('func', lambda x: x)(val)
                        obj[key] = val
                    csv_data.append(obj)

                if len(csv_data) == 0:
                    detail = f'File is empty or not valid: [{path}]'
                    logging.error(detail)
                    continue

                result.append(csv_data)

        return result
