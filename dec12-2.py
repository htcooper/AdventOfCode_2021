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
def findPaths(graph, small_caves, start, end, path):
    
    paths = []
    path = path + [start]
    
    if start == end:
        return [path]
    
    if start not in graph:
        print("start not in graph")
        return []
    
    for node in graph[start]:
        if node not in path:
            new_paths = findPaths(graph, small_caves, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
        elif node in path and node not in small_caves:
            new_paths = findPaths(graph, small_caves, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
        elif node in path and node in small_caves:
            check_set = set()
            check_flag = False
            for n in path:
                if n in small_caves and n not in check_set:
                    check_set.add(n)
                elif n in small_caves and n in check_set and check_flag==False: # will allow one duplicate
                    check_flag = True
            if check_flag == False:
                new_paths = findPaths(graph, small_caves, node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
    
    return paths

def prettyPrint(array):
    for row in array:
        for item in row:
            print(item, end = " ")
        print("")

def findAllPaths():
    graph, small_caves = buildGraph()
    all_paths = findPaths(graph, small_caves, start='start', end='end', path=[])
    num_paths = len(all_paths)
    #prettyPrint(all_paths)
    print(num_paths)
    return all_paths

findAllPaths()