import os
from array import *

## find last winning bingo board, and total all numbers not already pulled. Add those numbers together, and multiply by the last number pulled.

input_numbers = []
raw_data = []
puzzles = []

with open('input4.txt') as file:
    
    # separate the input numbers
    first_line = file.readline()
    first_line = first_line.split(',')

    for number in first_line:
        input_numbers.append(number.rstrip())    

    # put rest of lines into a big list
    for line in file:
        raw_data.append(line)

length = len(raw_data)
i = 1
single_puzzle = []

while i < length:
    if raw_data[i] != '\n':
        line = raw_data[i]
        a_line = line.strip().split()
        single_puzzle.append(a_line)
        if i == length-1:
            puzzles.append(single_puzzle)
            single_puzzle = []
    else:
        puzzles.append(single_puzzle)
        single_puzzle = []
    i += 1       

# now build a dict of dicts to hold necessary items
all_puzzle_dict = dict()
single_puzzle_dict = dict()
j = 0

puzzle_len = len(puzzles)

for puzzle in puzzles:
    single_puzzle_dict['first_row'] = puzzle[0]
    single_puzzle_dict['second_row'] = puzzle[1]
    single_puzzle_dict['third_row'] = puzzle[2]
    single_puzzle_dict['fourth_row'] = puzzle[3]
    single_puzzle_dict['fifth_row'] = puzzle[4]

    single_puzzle_dict['first_col'] = [puzzle[i][0] for i in range(5)]
    single_puzzle_dict['second_col'] = [puzzle[i][1] for i in range(5)]
    single_puzzle_dict['third_col'] = [puzzle[i][2] for i in range(5)]
    single_puzzle_dict['fourth_col'] = [puzzle[i][3] for i in range(5)]
    single_puzzle_dict['fifth_col'] = [puzzle[i][4] for i in range(5)]

    all_puzzle_dict[j] = single_puzzle_dict.copy()
    j += 1

# start loop with input numbers and add to set as they are "pulled". Then check for matches in any single puzzle dict.
pulled_numbers = set()
final_pulled_numbers = set()
winning_set = set()
unmarked_set = set()
winning_total = 0
last_winning_puzzle = all_puzzle_dict.copy()
remaining_winner = dict()
last_number_called = None

for number in input_numbers:
    pulled_numbers.add(number)

    for sp_key in all_puzzle_dict:
        sp_value = all_puzzle_dict[sp_key]
        for key in sp_value:
                
            value_set = sp_value[key]
            value_set = set(value_set)
            if value_set.issubset(pulled_numbers) and sp_key in last_winning_puzzle:
                remaining_winner['winner'] = all_puzzle_dict[sp_key]
                del last_winning_puzzle[sp_key]                    
                last_number_called = number    
                break

input_len = len(input_numbers)
i=0
final_pulled_numbers.add(last_number_called)
while input_numbers[i] != last_number_called:
    final_pulled_numbers.add(input_numbers[i])
    i += 1

for value in remaining_winner.values():
    for item in value.values():
        for num in item:
            winning_set.add(num)

for item in winning_set:
    if item not in final_pulled_numbers:
        item = int(item)
        winning_total += item

final_score = winning_total * int(last_number_called)
print(final_score)