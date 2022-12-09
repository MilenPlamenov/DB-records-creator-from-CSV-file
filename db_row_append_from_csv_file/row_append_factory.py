from reader import CsvReader
from db_performer import Performer


class RowAppendFactory:
    def __init__(self, table, *rows):
        self.table = table
        self.rows = rows

    def generate_records(self, reader: CsvReader, performer: Performer):
        csv_reader = reader
        csv_reader.read()

        db_performer = performer
        sql_statement = f'INSERT INTO {self.table} ({", ".join(self.rows)}) VALUES ' \
                        f'({", ".join(["%s"] * len(self.rows))})'
        # print(sql_statement)
        # print(self.rows)
        db_performer.execute(sql_statement, csv_reader.mapper)
