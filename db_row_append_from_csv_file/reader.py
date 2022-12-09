import csv


class CsvReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.mapper = []

    def read(self):
        file = open(self.file_name)
        csv_reader = csv.reader(file)
        [self.mapper.append(row) for row in csv_reader]
        file.close()

