
import statistics as st

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

def findClosingChar(char):
    closing_char = ''
    if char == '(':
        closing_char = ')'
    elif char == '[':
        closing_char = ']'
    elif char == '{':
        closing_char = '}'
    else:
        closing_char = '>'
    return closing_char 

def assignPenalty(char):
    penalty_table = {')': 1, ']': 2, '}': 3, '>': 4}
    return penalty_table[char]

def processLine(line):
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

    return line

all_lines = readFile()
closing_set = ('>','}',']',')')
score_list = []

for line in all_lines:
    
    line = processLine(line)
    is_incomplete = True
    
    for i in range(len(line)):
        if line[i] in closing_set:
            is_incomplete = False
            break
    
    if is_incomplete == True:
        score = 0
        closing_list = []
        line.reverse()

        for i in range(len(line)):
            closing_char = findClosingChar(line[i])
            closing_list.append(closing_char)
        
        for j in range(len(closing_list)):
            char_value = assignPenalty(closing_list[j])
            score *= 5
            score += char_value

        score_list.append(score)

med = st.median(score_list)
print(med)