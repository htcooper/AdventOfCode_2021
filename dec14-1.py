from collections import Counter

def readFile():
    master_list = []
    with open('input14-test.txt') as file:
        start_code = file.readline().strip()
        for line in file:
            line = line.rstrip()
            if line:
                letters = [s.strip() for s in line.split('->')]
                letters = tuple(letters)
                master_list.append(letters)
    master_list = tuple(master_list)
    return start_code, master_list

def insertLetter(x,y,master_list):
    xy = x + y
    for pair in master_list:
        if xy in pair:
            new_letter = pair[1]
            return new_letter

def makePass(start_list, code_string, master_list):
    new_code = code_string
    list_len = len(start_list)

    for i,s in enumerate(start_list):
        if i+1 < list_len:
            new_letter = insertLetter(start_list[i], start_list[i+1], master_list)
            new_code = new_code + new_letter + start_list[i+1]
    return new_code

start_code, master_list = readFile()
start_list = [c for c in start_code]
start_list = tuple(start_list)
code_string = start_list[0]    # start the list with the first letter
pass_count = 10
i=0

while i < pass_count:
    start_list = makePass(start_list, code_string, master_list)
    i+=1

most_common = Counter(start_list).most_common()[0]
least_common = Counter(start_list).most_common()[-1]

most_common_count = most_common[1]
least_common_count = least_common[1]

difference = most_common_count - least_common_count
print(difference)