import numpy as np
import copy
from queue import PriorityQueue

class Graph:
    def __init__(self):
        weights, width, height = readFile()
        self.weights = weights
        self.width = width
        self.height = height

def readFile():
    master_array = []
    with open('input15.txt') as file:
        for line in file:
            row = [int(c) for c in line.strip()]
            master_array.append(row)

    width = len(master_array[0])
    height = len(master_array)        
    return master_array, width, height

# builds the new, 5x larger graph and returns a single 2D array
def buildGraph(graph):
    init_array = graph.weights
    combined_array = copy.deepcopy(init_array)

    # create first mega-row of new graph
    for i in range(4):
        new_array = increment2Darray(init_array)
        combined_array = np.concatenate((combined_array, new_array), axis=1)
        init_array = new_array
        
    new_combined_array = copy.deepcopy(combined_array)

    # once we have the first mega-row, increment it 4 more times    
    for j in range(4):
        new_array = increment2Darray(combined_array)
        new_combined_array = np.concatenate((new_combined_array, new_array), axis=0)
        combined_array = new_array

    return new_combined_array

# takes an array of any size and increments all values by 1. After 9, values wrap around.
def increment2Darray(array):
    width = len(array[0])
    height = len(array)
    new_arr = [[0 for x in range(width)] for y in range(height)]

    for i in range(height):
        for j in range(width):
            new_arr[i][j] = array[i][j] + 1
            if new_arr[i][j] > 9:
                new_arr[i][j] = 1

    return new_arr

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

def heuristic(a,b):
    (x1,y1) = a
    (x2,y2) = b
    return abs(x1-x2) + abs(y1-y2)

# uses a* search with euclidian distance as the heuristic
def aStar(graph):
    width = len(graph[0])
    height = len(graph)

    start = (0,0)
    goal = (height-1,width-1)

    frontier = PriorityQueue()
    came_from = dict()
    cost_so_far = dict()

    came_from[start] = None
    cost_so_far[start] = 0

    frontier.put(start,0)
    
    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        successors = coordSuccessors(width,height,current)
        current_risk = cost_so_far[current]

        for successor in successors:
            i,j = successor[0], successor[1]
            s_risk = graph[i][j]
            new_risk = current_risk + s_risk

            if successor not in cost_so_far or new_risk < cost_so_far[successor]:
                cost_so_far[successor] = new_risk
                priority = new_risk + heuristic(successor, goal)
                frontier.put(successor,priority)
                came_from[next] = current

    return cost_so_far[goal]

g = Graph()
new_g = buildGraph(g)
final_cost = aStar(new_g)
print(final_cost)