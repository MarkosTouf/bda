import csv

    # Exercise 1.3.2:

with open('movies.csv', 'r', newline='') as file_incomplete:
    reader = csv.reader(file_incomplete)
    header =next(reader)

    expected_columns = len(header)

    for i, row in enumerate(reader):
        # print(f"Row {i}: {row}")
        if len(row) != expected_columns:
            print(f"Row {i} has {len(row)} columns, expected {expected_columns}.")
