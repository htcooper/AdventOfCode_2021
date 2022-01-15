from collections import defaultdict

# string is too large to actually construct. we will need to instead count the current number of pairs in the string, and the current count of characters in the string as we go. we don't need the actual string.

def readFile():
    master_pairs = {}   # build dict to map pairs to the inserted element
    with open('input14.txt') as file:
        start_code = file.readline().strip()
        for line in file:
            line = line.rstrip()
            if line:
                letters = [s.strip() for s in line.split('->')]
                master_pairs[letters[0]] = letters[1]
    #print(master_pairs)
    return start_code, master_pairs

def buildDicts(start_code):
    pairs = defaultdict(int)        # hold the current count of the letter pairs
    elements = defaultdict(int)     # hold the count of the individual elements/letters

    for i, el in enumerate(start_code[:-1]):    # count everything except for the last element (we're slicing into pairs)
        pairs[start_code[i:i+2]] += 1           # slice code into pairs
        elements[el] += 1                       # count each element

    elements[start_code[-1]] += 1   # add a count for the very last element in the initial string
    return pairs, elements

def runPasses(pairs, elements, master_pairs, num_passes):
    for i in range(num_passes):
        for pair, count in list(pairs.items()):
            new_element = master_pairs.get(pair)
            elements[new_element] += count  # increment the count for that element
            pairs[pair] -= count            # decrement the count of the pair being split apart
            pairs[pair[0] + new_element] += count   # construct the 2 new pairs created and add to the dictionary
            pairs[new_element + pair[1]] += count
    return elements     # we only need the element counts at the end

start_code, master_pairs = readFile()
pairs, elements = buildDicts(start_code)
final_elements = runPasses(pairs, elements, master_pairs, num_passes=40)

print(max(final_elements.values()) - min(final_elements.values()))
