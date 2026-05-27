# %%
# import csv

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)


# import csv

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row["genres"])


# import csv

# count = 0

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         if row["year"] == "2020":
#             count = count + 1 

# print(count)

# #exercise 2.1a
# import csv

# count = 0

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)

#     # for row in reader:
#     #     if "Action" in row["genres"]:
#     #         print(row)
#     #         break

#     # print(reader.fieldnames)

#     count = 0

    
## exercise 2.1b
# import csv

# count = 0

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)

#     # for row in reader:
#     #     if "Action" in row["genres"]:
#     #         print(row)
#     #         break

#     # print(reader.fieldnames)

#     count = 0

    
#     for row in reader:
#         if count < 5:
#             print(row)
#             count = count + 1


# exercise 2.1c

# import csv

# count = 0

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)

#     count = 0

#     for row in reader:
        
#         if "USA" in row["country"]:
#             print(row)
#             count = count + 1

#     print(count)


# exercise 2.1d

# import csv

# count = 0

# with open("movies.csv", "r") as file:
#     reader = csv.DictReader(file)

#     count = 0

#     for row in reader:
        
#         if row["genres"] == "Action":
#             print(row["title"])
#             break


#################################################

# exercise 2.1e

import csv

count = 0

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)

    count = 0

    for row in reader:
        
        if "Action" in row["genres"]:
            print(row["title"])
            break


# 2.1f: In one short comment, explain one benefit of DictReader over csv.reader.

# in the dictreader , we know the column name which relates to each value, so we know what the value represents.

# 2.1g: What are the time and space complexities of your script(s)?

# script 1: time complexity: O(1) space complexity: O(1)
# script 2: time complexity: O(1) space complexity: O(1)
# script 3: time complexity: O(n) space complexity: O(1)
# script 4: time complexity: O(n) space complexity: O(1)
# script 5: time complexity: O(n) space complexity: O(1)