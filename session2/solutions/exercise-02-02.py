
import csv

with open("studio_ghibli_movies.csv", "r") as file:
    file_reader = csv.DictReader(file)

#     # for row in file_reader:
#     #     print(row)

    for row_num, movie in enumerate(file_reader, start=1):
        # print(row_num, movie)

        # -- First find the missing values.

        for column in movie:
            # print(row[column])
            if movie[column].strip() == "":
                print(movie)
                print(f"For line {row_num} and movie {movie['title']} we have missing value for column {column}.")
                # print(row_num)
                # print(column)

        # -- Now fix the missing values.

        for column in movie:
            # print(row[column])
            if movie[column].strip() == "":
                print(movie)
                print(f" this is column {column} and has value '{movie[column]}'.") 

                if movie["title"] == "Howl's Moving Castle":
                    movie["music_by"] = "Hasao Miyasako"
                    print(f"This is fixed: {movie}")

                if movie["title"] == "Kiki's Delivery Service":
                    movie["year"] = "1989"
                    print(f"This is fixed: {movie}")

        # With list comprehensions just cleaning in place:

year_sum = 0
counter = 0
count_Miyazaki = 0

with open("studio_ghibli_movies.csv", "r") as file:

    file_reader_2 = csv.DictReader(file)

    with open("studio_ghibli_movies_clean.csv", "w") as file_to_write:

        writer = csv.DictWriter(file_to_write, file_reader_2.fieldnames)
        writer.writeheader()


        for movie in file_reader_2:

            if movie["year"].strip() == "" and movie["title"] == "Kiki's Delivery Service":
                movie["year"] = "1989"

            if movie["year"].strip() == "" and movie["title"] == "Ponyo":
                movie["year"] = "2001"

            if movie["music_by"].strip() == "" and movie["title"] == "Howl's Moving Castle":
                movie["music_by"] = "Hazy"

            if movie["director"] == "Hayao Miyazaki":
                count_Miyazaki += 1

            writer.writerow(movie)

            try:        

                year_sum += int(movie["year"])
                counter += 1
            
            except ValueError:
                pass

    print("year_sum:", year_sum)
    print("counter:", counter)
    print("average year is:", year_sum/counter)
    print("Count Miyazaki: ", count_Miyazaki)

    print(writer)

    with open("studio_ghibli_movies_clean.csv", "r") as file_cleaned:
        cleaned_reader = csv.DictReader(file_cleaned)

        for index, movie in enumerate(cleaned_reader):
            
            for attribute,value in movie.items():
                print(f"Movie {index}: {attribute}: {value}")

    with open("studio_ghibli_movies_clean.csv", "r") as file_cleaned:
        cleaned_check_reader = csv.DictReader(file_cleaned)

        for index, movie in enumerate(cleaned_check_reader):
            
            for attribute,value in movie.items():
                count_missing_values = 0
                if value == "":
                    print(f"For row {index} and movie {movie.get("title")} there is missing value.")
                    count_missing_values +=1

        print(f"count_missing_values:", count_missing_values)



# What is time and space complexity?

# time complexity is for n movies, m attributes . even if done several times it is essentially n * m.
# space complexity is either without using much memory due to the fact that the dictreader as well as files being iterable. 
# And when we write a file we use the hard drive to store it not the RAM.

        




        





