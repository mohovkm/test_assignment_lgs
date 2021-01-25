## Test assignment.
Full text of this test assignment you can find at [this url](https://gist.github.com/Attumm/3927bfab39b32d401dc0a4ca8db995bd#file-bank1-csv).

To run a program you need to use Python >= 3.6 (program checked on a python >= 3.8).
You don't need to use extra libraries or modules with this program.

run program:
`#> python3 app/main.py`

run tests:
```
#> cd app
#> python3 -m unittest tests/test_writer.py
#> python3 -m unittest tests/test_reader.py
```

Structure:
- **app**: root directory
- **app/classes**: all classes (readers, writers, handlers etc)
- **app/files**: folder with files to merge
- **app/logs**: program log files
- **app/main.py**: startup endpoint

To extend this program, you can use your own Reader/Writer classes, just inherit from Reader/Writer class and override "read"/"write" method
```python
class DBReader(Reader):
    def read(self) -> List[List[dict]]:
        pass

class DBWriter(Writer):
    def write(self, entity: List[dict]) -> None:
        pass
```

If you want to use different csv format to read data, you need to override `CSVFileReader._mapping` variable.
```python
_mapping = {
    'date': { # column name in output file 
        'aliases': ['timestamp'] # all column names in all files, that contains this format
        'func': lambda x: datetime.strptime(x, format) # function to transform data while read
    }
}
```
#### Warning!
CSVFileReader will read only columns, that added to `CSVFileReader._mapping[column]['aliases']`

If you want to use different csv format to write data, you need to override `CSVFileWriter._mapping` variable.
```python
_mapping = {
    'date': { # key name in dictionary 
        'func': lambda x: x.strftime('%Y-%m-%d') # function to transform data before writing
    }
}
```
#### Warning!
CSVFileWriter will write all data in merged entity. It uses `_mapping` only for data transformation before writing it to csv file.`
