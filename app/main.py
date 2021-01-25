from classes import CSVHandler, CSVFileReader, CSVFileWriter
from pathlib import Path
import logging


def configure_logging():
    logging_dir = Path('logs')
    logging_filename = Path('app.log')
    logging_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=logging_dir / logging_filename,
        level=logging.ERROR,
        format='%(asctime)s: %(levelname)s: %(message)s',
        datefmt='%m.%d.%Y %H:%I:%S'
    )


def main():
    configure_logging()

    # Collecting all csv files in folder
    csv_files_paths = list(Path('files').glob('*.csv'))

    # Reading collected files
    csv_data_in_dict = CSVHandler.read(
        CSVFileReader(csv_files_paths)
    )

    # Merging read files
    merged_data = CSVHandler.merge(csv_data_in_dict)

    out_file_path = Path('files/merged/merged.csv')

    # Writing merged files
    CSVHandler.write(
        CSVFileWriter(out_file_path),
        merged_data
    )


if __name__ == '__main__':
    main()
