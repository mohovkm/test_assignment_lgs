from classes import CSVHandler, CSVFileReader, CSVFileWriter
from pathlib import Path


def start_app():
    csv_files = list(Path('files').glob('*.csv'))
    csv_files = CSVHandler.read(
        CSVFileReader(csv_files)
    )

    for file in csv_files:
        print(file)

    # merged_data = CSVHandler.merge(csv_files)
    #
    # CSVHandler.write(
    #     CSVFileWriter('files/merged.csv'),
    #     merged_data
    # )


if __name__ == '__main__':
    start_app()
