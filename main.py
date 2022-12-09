import csv
import mysql.connector

file = open('db_row_append_from_csv_file/genre.csv')

csv_reader = csv.reader(file)

rows = []
for row in csv_reader:
    rows.append(row)

file.close()

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="testdb"
)

my_cursor = db.cursor()

sql = "INSERT INTO genre (genre_id, name) VALUES (%s, %s)"

my_cursor.executemany(sql, rows)

db.commit()

print(my_cursor.rowcount, "rows were inserted.")

# fast implementation not recommended
