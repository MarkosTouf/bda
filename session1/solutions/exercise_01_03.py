import csv

# with open('movies.csv', 'r', newline='') as file:
#     reader = csv.reader(file)

#     # print(reader)

#     # for row in reader:
#     #     if len(row) > 4:
#     #         print(row[4])

#     # for row in reader:
#     #     print(row)
#     #     print(len(row))

#     # 1. to print the header row

#     # reader = next(reader)
#     # print(reader)

#     # 2. to print the first 5 rows of the data

#     # for i in range(5):
#     #     print(reader[i]) 



#     # 3. Find and print the first movie where genres contains Action, then stop.

#     with open('movies.csv', 'r', newline='') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header row
        
#         for row in reader:
#             if "Action" in row[4]:
#                 print(row[1])
#                 break

    # 4.benefit and drawback of csv.reader() raw
    # a benefit is that it returns iterator and I take and use in memory one line at a time.
    # a drawback is that it uses indexing to access the data which is not very readable and may cause errors if the structure of the data changes.

    # 5. complexities time and space.
    # time complexity is O(n) because if we double the data we at worst scenario may require to process double the tasks.
    # space complexity is O(1) becuase we store and use in memory one process at a time.


    # Exercise 1.3.2:

with open('movies_incomplete.csv', 'r', newline='') as file_incomplete:
    reader = csv.reader(file_incomplete)
    header =next(reader)

    expected_columns = len(header)

    for i, row in enumerate(reader):
        # print(f"Row {i}: {row}")
        if len(row) != expected_columns:
            print(f"Row {i} has {len(row)} columns, expected {expected_columns}.")
