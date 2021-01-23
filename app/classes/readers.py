import csv
from abc import ABC, abstractmethod
from typing import List, Union
from pathlib import Path
from decimal import Decimal
from .parser import Parser


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
        self.files = files

    def read(self) -> List[List[dict]]:
        """

        :return:
        """
        result = []

        for path in self.files:
            path = Path(path)
            if not path.is_file():
                print(f'{path} is not a file')

            with open(path, mode='r') as f:
                csv_reader = csv.DictReader(f)
                csv_data = []

                for row in csv_reader:
                    obj = {}

                    for key, value in self._mapping.items():
                        val = None
                        aliases = [x for x in value.get('aliases', []) if x in row]
                        if len(aliases) == 0:
                            continue

                        if len(aliases) > 1 and value.get('concat', False):
                            values_to_concat = []
                            for alias in value.get('concat'):
                                values_to_concat.append(row[alias])
                            val = '.'.join(values_to_concat)

                        if val is None:
                            alias = aliases[0]
                            val = value.get('func', lambda x: x)(row[alias])
                        else:
                            val = value.get('func', lambda x: x)(val)
                        obj[key] = val
                    csv_data.append(obj)

                result.append(csv_data)

        return result
