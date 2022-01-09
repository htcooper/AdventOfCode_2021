# 0: 6 elements: abcefg
# 1: 2 elements: cf
# 2: 5 elements: acdeg
# 3: 5 elements: acdfg
# 4: 4 elements: bcdf
# 5: 5 elements: abdfg
# 6: 6 elements: abdefg
# 7: 3 elements: acf
# 8: 7 elements: abcdefg
# 9: 6 elements: abcdfg

# unique: 1 (2 elements), 4 (4 elements), 7 (3 elements), 8 (7 elements)
# 6 elements (0, 6, 9)
# 5 elements (2, 3, 5)

counter = 0
unique_vals = {2,4,3,7}
values = []
with open('input8.txt') as file:
    for line in file:
        first = [c.strip() for c in line.split('|')]
        values.append(first)

for vals in values:
    output_vals = vals[1].split()
    for v in output_vals:
        if len(v) in unique_vals:
            counter += 1
    
print(counter)