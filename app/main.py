from classes import CSVHandler, CSVFileReader, CSVFileWriter
from pathlib import Path


def start_app():
    csv_files_paths = list(Path('files').glob('*.csv'))
    csv_data_in_dict = CSVHandler.read(
        CSVFileReader(csv_files_paths)
    )

    merged_data = CSVHandler.merge(csv_data_in_dict)

    out_file_path = Path('files/merged.csv')

    CSVHandler.write(
        CSVFileWriter(out_file_path),
        merged_data
    )


if __name__ == '__main__':
    start_app()
