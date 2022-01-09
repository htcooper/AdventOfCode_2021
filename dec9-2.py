from collections import deque as dq
import math

def readFile():
    master_list = []
    with open('input9.txt') as file:
        for line in file:
            numbers = [int(s) for s in line.strip()]
            master_list.append(numbers)
    return master_list

def getLen(item):
    return len(item)

def coordSuccessors(width, height, coords):
    i,j = coords[0], coords[1]
    coords = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]

    if i == 0:
        coords.remove((i-1, j))
    elif i == height-1:
        coords.remove((i+1, j))
    if j == 0:
        coords.remove((i, j-1))
    elif j == width-1:
        coords.remove((i, j+1))

    return coords   # list of tuples

# use bfs to find basins

def solvePuzzle2():
    frontier = dq()     # frontier queue
    explored = set()    # set of explored states
    current_basin = set()   # set of current basin coordinates
    all_basins = []     # store all basins for sorting by size later

    master_list = readFile()  
    width = len(master_list[0])
    height = len(master_list)

    for i,row in enumerate(master_list):
        for j,value in enumerate(row):

            current_location = (i,j)
            if current_location not in explored:
                explored.add(current_location)

                if value < 9:
                    current_basin.add(current_location)
                    frontier.append(current_location)

            while len(frontier) > 0:
                current_location = frontier.popleft()
                coords = coordSuccessors(width, height, current_location)                

                for coord in coords:
                    if coord not in explored:
                        explored.add(coord)

                        if master_list[coord[0]][coord[1]] < 9:
                            current_basin.add(coord)
                            frontier.append(coord)
                
            if len(frontier) == 0:
                if current_basin:                       # prevents adding empty set to list
                    all_basins.append(current_basin)    # we've found everything in the basin
                    current_basin = set()               # reset current basin
    
    all_basins.sort(key=getLen, reverse=True)           # sort basins by size descending
    total_size = 0
    basin_size_list = []

    for i in range(3):                                  # get the top 3 sizes
        basin_size = len(all_basins[i])
        basin_size_list.append(basin_size)

    total_size = math.prod(basin_size_list)
    print(total_size)

solvePuzzle2()