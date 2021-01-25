from datetime import datetime
from typing import Union


class Parser:
    @staticmethod
    def parse_data(date: str, formats: list) -> Union[datetime, None]:
        """Parse string with given formats

        :param date: (str) - string with date
        :param formats: (list) - all possible formats, that date may look like
        :return:
        """
        parsed_date = None
        for fmt in formats:
            try:
                parsed_date = datetime.strptime(date, fmt)
                break
            except ValueError as _:
                continue

        return parsed_date
