import csv
from abc import ABC, abstractmethod
from typing import List
from pathlib import Path


class Writer(ABC):
    @abstractmethod
    def write(self, entity: dict) -> None:
        pass


class CSVFileWriter(Writer):
    def __init__(self, path: str):
        self.path = path

    def write(self, entity: dict) -> None:
        pass
