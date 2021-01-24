import csv
from abc import ABC, abstractmethod
from typing import List, Union
from pathlib import Path
import os


class Writer(ABC):
    @abstractmethod
    def write(self, entity: List[dict]) -> None:
        pass


class CSVFileWriter(Writer):
    _mapping = {
        'date': {
            'func': lambda x: x.strftime('%Y-%m-%d')
        }
    }

    def __init__(self, path: Union[str, Path]):
        self.path = path

    def write(self, entity: List[dict]) -> None:
        """

        :param entity:
        :return:
        """
        path = Path(self.path)
        try:
            rindex = str(path).rindex(os.sep)
            Path(str(path)[:rindex]).mkdir(parents=True, exist_ok=True)
        except ValueError as _:
            pass

        if len(entity) == 0:
            return

        with open(path, 'w') as f:
            fieldnames = entity[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            for row in entity:
                for key, value in self._mapping.items():
                    if key in row:
                        row[key] = value['func'](row[key])
                writer.writerow(row)
