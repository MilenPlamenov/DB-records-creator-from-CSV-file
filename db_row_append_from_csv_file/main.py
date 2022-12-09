from db_row_append_from_csv_file.db_performer import Performer
from db_row_append_from_csv_file.reader import CsvReader
from row_append_factory import RowAppendFactory

"""

CSV -> DB records converter

main() attrs params:
    RowAppendFactory(table name, *args->all table columns)
    generate_records(csv file, db host, db user, db password, database)
    
    https://generatedata.com/generator -> data generator (max 500)
    
"""


def main():
    factory = RowAppendFactory('genre', 'genre_id', 'name')
    factory.generate_records(
        CsvReader('genre.csv'),
        Performer('localhost', 'admin', 'admin', 'testdb'),
    )


if __name__ == "__main__":
    main()


