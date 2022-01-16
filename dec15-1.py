
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
    #print(master_array)
    return master_array, width, height

# uses dynamic programming
def minCost(graph):
    min_graph = [[float('inf') for x in range(graph.width)] for y in range(graph.height)]

    # set starting value
    min_graph[0][0] = 0

    # fill first column
    for i in range(1,graph.height):
        prev_cost = min_graph[i-1][0]
        min_graph[i][0] = prev_cost + graph.weights[i][0]

    # fill top row
    for j in range(1,graph.width):
        prev_cost = min_graph[0][j-1]
        min_graph[0][j] = prev_cost + graph.weights[0][j]

    # fill in the rest of the graph
    for i in range(1,graph.height):
        for j in range(1, graph.width):
            prev_cost_up = min_graph[i-1][j]
            prev_cost_left = min_graph[i][j-1]
            if i+1 < graph.height:
                prev_cost_down = min_graph[i+1][j]
            if j+1 < graph.width:
                prev_cost_right = min_graph[i][j+1]

            min_graph[i][j] = graph.weights[i][j] + min(prev_cost_left, prev_cost_up, prev_cost_right, prev_cost_down)

    #print(min_graph)

    final_cost = min_graph[graph.height-1][graph.width-1]
    return final_cost

g = Graph()
print(minCost(g))