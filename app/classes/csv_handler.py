from typing import List
from .readers import Reader
from .writers import Writer
from functools import reduce
import logging


class CSVHandlerException(Exception):
    pass


class CSVHandlerTypeError(CSVHandlerException):
    pass


class CSVHandler:
    @staticmethod
    def merge(entities: List[List[dict]]) -> List[dict]:
        """Method to merge lists with dicts (List[List[dict]]) into single list with dicts [List[dict]]

        :param entities: (List[List[dict]]) - entities to merge
        :return: List[dict] - merged entity
        """
        if len(entities) == 0:
            detail = 'Can\'t merge an empty list.'
            logging.error(detail)
            return entities

        if not isinstance(entities, list):
            detail = f'Entities must be type of a [list] got [{type(entities)}] instead.'
            logging.error(detail)
            raise CSVHandlerTypeError(detail)

        return list(reduce(lambda x, y: [*x, *y], entities))

    @staticmethod
    def read(reader: Reader) -> List[list]:
        """Reader Handler.

        :param reader: (Reader) - reader instance
        :return:
        """
        csv_data = reader.read()
        return csv_data

    @staticmethod
    def write(writer: Writer, entity: List[dict]) -> None:
        """Writer handler.

        :param writer: (Writer) - Writer instance.
        :param entity: (List[dict]) entity to write.
        :return: None
        """
        writer.write(entity)

