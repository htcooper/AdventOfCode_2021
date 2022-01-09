import collections as col

inputs = []

with open('input5.txt') as file:

    # extract numbers and place in tuple - only take horizontal or vertical lines
    for line in file:
        line = line.replace('->',',')
        line = line.replace(',',' ')
        numbers = [int(s) for s in line.split() if s.isdigit()]
        x1 = numbers[0]
        y1 = numbers[1]
        tuple_1 = (x1,y1)
        x2 = numbers[2]
        y2 = numbers[3]
        tuple_2 = (x2,y2)
        inputs.append((tuple_1, tuple_2))

counter_list = []

for ts in inputs:
    start_x = ts[0][0]
    start_y = ts[0][1]
    end_x = ts[1][0]
    end_y = ts[1][1]

    if start_x == end_x:
        if start_y < end_y:
            end = end_y + 1
            for i in range(start_y, end, 1):
                new_tuple = (start_x, i)
                counter_list.append(new_tuple)

        else:
            end = start_y + 1
            for i in range(end_y, end, 1):
                new_tuple = (start_x, i)
                counter_list.append(new_tuple) 

    elif start_y == end_y:
        if start_x < end_x:
            end = end_x + 1
            for i in range(start_x, end):
                new_tuple = (i, start_y)
                counter_list.append(new_tuple)

        else:
            end = start_x + 1
            for i in range(end_x, end):
                new_tuple = (i, start_y)
                counter_list.append(new_tuple)

    elif abs(start_x-end_x) == abs(start_y-end_y): # deal with 45 degree diagonals
        # figure out which direction the diagonal is going

        diag_range = abs(start_x-end_x)

        if start_x < end_x and start_y < end_y:
            for i in range(diag_range+1):
                new_tuple = (start_x+i, start_y+i)
                counter_list.append(new_tuple)

        elif start_x > end_x and start_y < end_y:
            for i in range(diag_range+1):
                new_tuple = (start_x-i, start_y+i)
                counter_list.append(new_tuple)

        elif start_x < end_x and start_y > end_y:
            for i in range(diag_range+1):
                new_tuple = (start_x+i, start_y-i)
                counter_list.append(new_tuple)

        else:
            for i in range(diag_range+1):
                new_tuple = (start_x-i, start_y-i)
                counter_list.append(new_tuple)

number_counter = col.Counter(t for t in counter_list)

total_count = 0

for t in number_counter:
    if number_counter[t] >= 2:
        total_count += 1

print(total_count)