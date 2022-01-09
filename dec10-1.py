
def readFile():
    master_list = []
    with open('input10.txt') as file:
        for line in file:
            chars = [c for c in line.strip()]
            master_list.append(chars)
    return master_list

def matchingPairs(list,i,j):
    if list[i] == '<' and list[j] =='>':
        return True
    if list[i] == '(' and list[j] ==')':
        return True
    if list[i] == '{' and list[j] =='}':
        return True
    if list[i] == '[' and list[j] ==']':
        return True

    return False

def assignPenalty(char):
    penalty_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return penalty_table[char]

all_lines = readFile()
closing_set = ('>','}',']',')')
penalty_list = []
total_score = 0

for line in all_lines:
    j = 0
    found_match = True

    while found_match == True:

        if j == len(line)-2:
            found_match = False

        if matchingPairs(line,j,j+1):
            del line[j+1]
            del line[j]
            found_match = True
            j = 0

        else:
            if j < len(line)-2:
                j += 1
    
    for i in range(len(line)):
        if line[i] in closing_set:
            current_penalty = assignPenalty(line[i])
            penalty_list.append(current_penalty)
            break

total_score = sum(penalty_list)
print(total_score)