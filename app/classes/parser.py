from datetime import datetime
from typing import Union


class Parser:
    @staticmethod
    def parse_data(date, formats: list) -> Union[datetime, None]:
        """

        :param date:
        :param formats:
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
