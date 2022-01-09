from collections import defaultdict as dd

def readFile():
    master_list = []
    small_caves = set() # can only visit small caves once per path
    with open('input12.txt') as file:
        for line in file:
            numbers = [s.strip() for s in line.split('-')]
            master_list.append(numbers)
            for n in numbers:
                if n.islower() and n != 'start' and n != 'end':
                    small_caves.add(n)

    return master_list, small_caves

def buildGraph():
    edge_list, small_caves = readFile()
    graph = dd(list)

    for edge in edge_list:
        i,j = edge[0], edge[1]

        # create adjacency list
        if j == 'start':    # reverse path if endpoint is start
            graph[j].append(i)
        else:
            graph[i].append(j)
            if i != 'start' and j != 'end':  # don't need to reverse direction at end points
                graph[j].append(i)

    return graph, small_caves
        
# use Djikstra's algorithm
def findPaths(graph, small_caves, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        print("start not in graph")
        return []
    paths = []
    for node in graph[start]:
        if node not in path or (node in path and node not in small_caves):
            new_paths = findPaths(graph, small_caves, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def findAllPaths():
    graph, small_caves = buildGraph()
    all_paths = findPaths(graph, small_caves, start='start', end='end', path=[])
    num_paths = len(all_paths)
    print(num_paths)
    return all_paths


findAllPaths()