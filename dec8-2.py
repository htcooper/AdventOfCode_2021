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

# this solution uses set overlaps to determine the values

unique_vals = {2,4,3,7}
values = []
guide = {}
total = 0

with open('input8.txt') as file:
    for line in file:
        first = [c.strip() for c in line.split('|')]
        values.append(first)

for vals in values:
    input_vals = vals[0].split()
    output_vals = vals[1].split()
    
    # need to find the unique values first
    for v in input_vals:
        vlen = len(v)
        if vlen in unique_vals:   # we know it is 1, 4, 7, or 8 -- need to get these first
            if vlen == 2:          # we know this is 1
                v = set(v)
                guide[1] = v
            elif vlen == 4:
                v = set(v)
                guide[4] = v
            elif vlen == 3:
                v = set(v)
                guide[7] = v
            else:
                v = set(v)
                guide[8] = v
    
    # once we have the unique vals, we can use the set relationships to determine the rest    
    for v2 in input_vals:
        v2len = len(v2)
       
        if v2len == 6:     # we know this is 0, 6, or 9
            v2 = set(v2)
            if guide[4].issubset(v2):   # we know this is 9
                guide[9] = v2
            elif len(v2 & guide[1]) == 1:     # we know this is 6
                guide[6] = v2
            else:
                guide[0] = v2

        elif v2len == 5:    # we know this is 2, 3, or 5
            v2 = set(v2)
            if guide[1].issubset(v2):   # we know this is 3
                guide[3] = v2
            elif len(v2 & guide[4]) == 2:   # we know this is 2
                guide[2] = v2
            else:
                guide[5] = v2

    string_nums = ''

    for ovals in output_vals:
        ovals = set(ovals)
        for key in guide.keys():
            if ovals == guide[key]:
                key = str(key)
                string_nums += key

    string_nums = int(string_nums)
    total += string_nums

print(total)
