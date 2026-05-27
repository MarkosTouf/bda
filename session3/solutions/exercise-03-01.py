# with open("les_miserables.txt", "r", encoding="utf-8") as file:

#     for line_num, line in enumerate(file, start=1):
#         # print(line_num, line)

#         if "Jean Valjean" in line:
#             print("line number is:",line_num)
#             print("Full line is:", line)
#             break

# Jean Valjean


# -- find the line count.

with open("les_miserables.txt", "r", encoding="utf-8") as file:

    line_count = 0

    for line_num, line in enumerate(file, start=1):
        # print(line_num, line)

        line_count = line_num

print(line_num)


# -- Compute the average line length.

with open("les_miserables.txt", "r", encoding="utf-8") as file:

    count_lines = 0
    sum_line_lengths = 0

    for line_num, line in enumerate(file, start=1):
    
        count_lines = line_num

        sum_line_lengths += len(line)

    avg_line_length = sum_line_lengths / count_lines

    print(avg_line_length)



        


