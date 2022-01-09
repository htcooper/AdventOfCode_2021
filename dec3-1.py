diagnostic_codes = []

with open('input3.txt') as file:
    for line in file:
        line = line.rstrip()
        diagnostic_codes.append(line)


length = len(diagnostic_codes[0])
gamma = []
epsilon = []
i = 0

while i<length:
    zero_count = 0
    one_count = 0
    total_count = 0

    for code in diagnostic_codes:
        i_char = code[i]
        total_count += 1

        if i_char == '0':
            zero_count += 1

    one_count = total_count - zero_count
    if one_count > zero_count:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')
            
    i += 1
  
gamma = ''.join(gamma)
epsilon = ''.join(epsilon)

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

final_rate = gamma * epsilon

print(f"gamma is {gamma} and epsilon is {epsilon} and final rate is {final_rate}") 
            

