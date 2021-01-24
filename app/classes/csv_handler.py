from typing import List
from .readers import Reader
from .writers import Writer
from functools import reduce


class CSVHandler:
    @staticmethod
    def merge(entities: List[List[dict]]) -> List[dict]:
        """

        :param entities:
        :return:
        """
        return list(reduce(lambda x, y: [*x, *y], entities))

    @staticmethod
    def read(reader: Reader) -> List[list]:
        """

        :param reader:
        :return:
        """
        csv_data = reader.read()
        return csv_data

    @staticmethod
    def write(writer: Writer, entity: List[dict]) -> None:
        """

        :param writer:
        :param entity:
        :return:
        """
        writer.write(entity)


# csv_files = CSVHandler.read(
#     CSVFileReader(['../files/bank1.csv'])
# )
#
# print(csv_files)

# merged_data = CSVHandler.merge(csv_files)
#
# CSVHandler.write(
#     CSVFileWriter('files/merged.csv'),
#     merged_data
# )
