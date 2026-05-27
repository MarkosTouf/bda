

from exercise_01_02_lib import mylen

print(mylen([10, 20, 30]))

##################################################

data = [10, 20, 30, 40, 50]

total = 0

for i in range(len(data)):
    total = total + data[i]

print(total)

##################################################

data = [10, 20, 30, 40, 50]

number_check = 50

pointer = -1

for i in range(len(data)):

    if data[i] == number_check:
        pointer = i
        break
        
print(pointer)

##################################################

matrix = [
    [10, 20],
    [30, 40]
]

for row in matrix:
    print(row)
    for value in row:
        print(value)

################################################

matrix = [
    [10, 20],
    [30, 40]
]

row_index = 0
col_index = 0

for row in matrix:
    print("row:", row_index)
    for value in row:
        print("col:", col_index, "value:", value)
        col_index += 1
    # Reset col_index for each new row.
    col_index = 0
    row_index += 1


##Task1


data = [30, 6, 9, 12, 15, 8]

def count_in_range(data, lower_bound, upper_bound):

    counter = 0

    for i in range(len(data)):
        if data[i]>=lower_bound and data[i]<=upper_bound:
            counter = counter+1

    return counter
    
counter_output = count_in_range(data,1,10)
print(counter_output)

##Task2

data = [30, 6, 9, 12, 15, 8]


def sum_even_numbers(data):

    total = 0
    for num in data:
        if num%2==0:
            total = total+num
    return total
        
total_output = sum_even_numbers(data)

print(total_output)


##Task3

data = [30, 6, 9, 12, 15, 8]


def position_of_number(data_input, number):
    position = -1
    
    for i in range(len(data)):
        
        if data[i] == number:
            position = i
            return position
            break
    return position
    

position_output = position_of_number(data,12)

print(position_output)



