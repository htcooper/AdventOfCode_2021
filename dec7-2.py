# binomial sequence n*(n+1)/2

import statistics as st
import math
import numpy as np

with open('input7.txt') as file:
    for line in file:
        numbers = [int(s) for s in line.split(',')]

fuel = 0
fuel_alt = 0
cmean = math.ceil(st.mean(numbers))
fmean = math.floor(st.mean(numbers))

for num in numbers:
    n = abs(cmean-num)
    binom = (n*(n+1)) / 2
    fuel += binom

for num in numbers:
    n = abs(fmean-num)
    binom = (n*(n+1)) / 2
    fuel_alt += binom

solution = 0
if fuel <= fuel_alt:
    solution = fuel
else:
    solution = fuel_alt

print(int(solution))