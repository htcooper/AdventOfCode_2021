# find median

import statistics as st

with open('input7.txt') as file:
    for line in file:
        numbers = [int(s) for s in line.split(',')]

median = st.median(numbers)
solution = 0

for num in numbers:
    fuel = abs(median - num)
    solution += fuel

print(int(solution))