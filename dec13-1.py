
# coordinates are (x,y) with (0,0) in top left

#fold along x=655
#fold along y=447
#fold along x=327
#fold along y=223
#fold along x=163
#fold along y=111
#fold along x=81
#fold along y=55
#fold along x=40
#fold along y=27
#fold along y=13
#fold along y=6


def readFile():
    master_list = []
    with open('input13.txt') as file:
        for line in file:
            numbers = [int(s.strip()) for s in line.split(',')]
            numbers = tuple(numbers)
            master_list.append(numbers)
    #print(master_list)        
    return master_list

def foldHorizontal(y_fold, coords):
    new_coords = []
    for coord in coords:
        if coord[1] < y_fold:   # if y is above the fold, leave alone
            new_coords.append(coord)
        else:
            diff = abs(y_fold - coord[1])
            new_y = y_fold - diff
            new_coords.append((coord[0], new_y))

    # clean up overlaps
    new_coords = set(new_coords)
    new_coords = list(new_coords)

    return new_coords

def foldVertical(x_fold, coords):
    new_coords = []
    for coord in coords:
        if coord[0] < x_fold:   # if x is to the left of the fold, leave alone
            new_coords.append(coord)
        else:
            diff = abs(x_fold - coord[0])
            new_x = x_fold - diff
            new_coords.append((new_x, coord[1]))

    # clean up overlaps
    new_coords = set(new_coords)
    new_coords = list(new_coords)

    return new_coords



coords = readFile()
new_coords = foldVertical(655, coords)
num = len(new_coords)
print(num)
