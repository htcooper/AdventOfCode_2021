
def readFile():
    # convert input to 2D list
    master_list = []
    with open('input11.txt') as file:
        for line in file:
            numbers = [int(s) for s in line.strip()]
            master_list.append(numbers)
    return master_list

# determine coordinate possibilities
def coordSuccessors(width, height, coords):
    i,j = coords[0], coords[1]
    adj_coords = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]

    if i == 0:          # top row
        adj_coords.remove((i-1, j-1))
        adj_coords.remove((i-1, j))
        adj_coords.remove((i-1, j+1))
    elif i == height-1: # bottom row
        adj_coords.remove((i+1, j-1))
        adj_coords.remove((i+1, j))
        adj_coords.remove((i+1, j+1))
    if j == 0:          # first column 
        adj_coords.remove((i, j-1))
        if i != height-1:   # keep from removing twice if corner coordinate
            adj_coords.remove((i+1, j-1))
        if i != 0:          # keep from removing twice if corner coordinate
            adj_coords.remove((i-1, j-1))
    elif j == width-1:  # last column
        adj_coords.remove((i, j+1))
        if i != 0:          # keep from removing twice if corner coordinate
            adj_coords.remove((i-1, j+1))
        if i != height-1:   # keep from removing twice if corner coordinate
            adj_coords.remove((i+1, j+1))
    
    return adj_coords   # list of tuples

# recursively flash without incrementing values that have already flashed
def flash(master_list, current_coord, flashed_set): 
    width = len(master_list[0])
    height = len(master_list)    
    coords = coordSuccessors(width, height, current_coord)

    for coord in coords:
        i,j = coord[0], coord[1]
        if (i,j) not in flashed_set:
            master_list[i][j] += 1
        if master_list[i][j] > 9:
            master_list[i][j] = 0
            flashed_set.add((i,j))
            flash(master_list, (i,j), flashed_set)
    
    return flashed_set

master_list = readFile()
flash_count = 0
step_counter = 0

# find step at which all flashes happen simultaneously
while flash_count != 100:
    step_counter += 1
    flashed_set = set() # reset for every loop
    for i,row in enumerate(master_list):
        for j,value in enumerate(row):

            if (i,j) not in flashed_set:
                master_list[i][j] += 1
            if master_list[i][j] > 9:
                master_list[i][j] = 0
                flashed_set.add((i,j))
                new_flashes = flash(master_list, (i,j), flashed_set)
                flashed_set = flashed_set | new_flashes
            
    flash_count = len(flashed_set)

print(step_counter)
