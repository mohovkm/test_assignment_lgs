import csv
from abc import ABC, abstractmethod
from typing import List, Union
from pathlib import Path
import os
import logging


class Writer(ABC):
    @abstractmethod
    def write(self, entity: List[dict]) -> None:
        pass


class CSVFileWriterException(Exception):
    pass


class CSVFileWriterTypeError(CSVFileWriterException):
    pass


class CSVFileWriter(Writer):
    _mapping = {
        'date': {
            'func': lambda x: x.strftime('%Y-%m-%d')
        }
    }

    def __init__(self, path: Union[str, Path]):
        """Initialisation

        :param path: path to file, to write merged data
        """
        if not isinstance(path, str) and not isinstance(path, Path):
            detail = f'Path must be an instance of [str, Path] got [{type(path)}] instead.'
            raise CSVFileWriterTypeError(detail)

        self.path = path

    def write(self, entity: List[dict]) -> None:
        """Writer implementation.
        Method uses csv.DictWriter to write entity to file.

        :param entity: List[dict] - list with dict data, where every dict in list is a new row in the csv file.
        :return: None
        """
        path = Path(self.path)
        try:
            rindex = str(path).rindex(os.sep)
            Path(str(path)[:rindex]).mkdir(parents=True, exist_ok=True)
        except ValueError as _:
            pass

        if len(entity) == 0:
            detail = 'Entity is empty'
            logging.error(detail)
            return

        with open(path, 'w') as f:
            fieldnames = entity[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            for row in entity:
                for key, value in self._mapping.items():
                    if key in row and row[key] is not None:
                        row[key] = value['func'](row[key])
                writer.writerow(row)
