from typing import List
from .readers import Reader
from .writers import Writer


class CSVHandler:
    @staticmethod
    def merge(entities: List[dict]) -> dict:
        """

        :param entities:
        :return:
        """
        # self.entity = {}
        return {}

    @staticmethod
    def read(reader: Reader) -> List[list]:
        """

        :param reader:
        :return:
        """
        csv_data = reader.read()
        return csv_data

    @staticmethod
    def write(writer: Writer, entity: dict) -> None:
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
