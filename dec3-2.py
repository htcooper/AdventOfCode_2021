import copy

diagnostic_codes = []

with open('input3.txt') as file:
    for line in file:
        line = line.rstrip()
        diagnostic_codes.append(line)

length = len(diagnostic_codes[0])
oxygen_rating = copy.deepcopy(diagnostic_codes)
co2_scrubber_rating = copy.deepcopy(diagnostic_codes)

bit_position = 0

while len(oxygen_rating) > 1:

    if bit_position == length:
        bit_position = 0

    zero_count = 0
    one_count = 0
    total_count = 0
    one_list = []
    zero_list = []

    for code in oxygen_rating:
        bit = code[bit_position]
        total_count += 1

        if bit == '0':
            zero_count += 1
            zero_list.append(code)

        elif bit == '1':
            one_count += 1
            one_list.append(code)

    # To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. 
    # If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    if one_count >= zero_count:
        oxygen_rating = copy.deepcopy(one_list)

    elif one_count < zero_count:
        oxygen_rating = copy.deepcopy(zero_list)

    bit_position += 1

final_ox_rating = oxygen_rating[0]
final_ox_rating = int(final_ox_rating, 2)
print(f"oxygen rating is {oxygen_rating} with value {final_ox_rating}")

bit_position = 0

while len(co2_scrubber_rating) > 1:

    if bit_position == length:
        bit_position = 0

    zero_count = 0
    one_count = 0
    total_count = 0
    one_list = []
    zero_list = []
    

    for code in co2_scrubber_rating:
        bit = code[bit_position]
        total_count += 1

        if bit == '0':
            zero_count += 1
            zero_list.append(code)

        elif bit == '1':
            one_count += 1
            one_list.append(code)

    # To find co2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. 
    # If 0 and 1 are equally common, keep values with a 0 in the position being considered.
    if one_count >= zero_count:
        co2_scrubber_rating = copy.deepcopy(zero_list)

    elif one_count < zero_count:
        co2_scrubber_rating = copy.deepcopy(one_list)

    bit_position += 1

final_co2_rating = co2_scrubber_rating[0]
final_co2_rating = int(final_co2_rating, 2)

print(f"co2_scrubber_rating is {co2_scrubber_rating} with value {final_co2_rating}")

final_total = final_ox_rating * final_co2_rating
print(f"final total is {final_total}")
















            

