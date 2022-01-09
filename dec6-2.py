# preprocess input
with open('input6.txt') as file:
    for line in file:
        numbers = [int(s) for s in line.split(',') if s.isdigit()]

current_list = tuple(numbers)
cycles = 256
count = 0

current_states = {
    0: current_list.count(0),
    1: current_list.count(1),
    2: current_list.count(2),
    3: current_list.count(3),
    4: current_list.count(4),
    5: current_list.count(5),
    6: current_list.count(6),
    7: current_list.count(7),
    8: current_list.count(8)
    }

for i in range(cycles):

    next_states = {}
    
    next_states = {
        0: current_states[1],
        1: current_states[2],
        2: current_states[3],
        3: current_states[4],
        4: current_states[5],
        5: current_states[6],
        6: current_states[7],
        7: current_states[8],
        8: current_states[0]
    }

    # add the zero fish to the 6-day fish
    if current_states[0] > 0:
        next_states[6] += current_states[0]

    current_states = next_states
    
for fish in current_states:
    count += current_states[fish]    

print(count)