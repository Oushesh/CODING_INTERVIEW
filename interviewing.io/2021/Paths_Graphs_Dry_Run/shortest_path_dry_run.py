'''
Given is the following pair of edges:
1. Build the graph using defaultdict(set)
2. Find path start to goal
3. Find all paths from start to goal
4. Find shortest path from start to goal
5. DFS start to goal

#Reference for the dry run:
'''

'''
visited = {} as a set data strucure
Classical DFS solution below
'''

from collections import defaultdict


def dfs(graph, visited, start, goal):
    # Test graph validity
    assert (len(graph) > 0)
    if start not in visited and not start == goal:
        visited.add(start)

    for neighbour in graph[start]:
        if not neighbour == goal:
            if neighbour not in visited:
                visited.add(neighbour)
                return dfs(graph, visited, neighbour, goal)
        else:
            return neighbour


'''
Find path start to goal.
The idea is to recursively add the 
the new visited nodes to the path.
Obviously path is to be represented as
a list.
'''


def find_path(graph, start, end, path=[], visited=set()):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        print('invialid graph')
        return None
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
        if node not in path:
            current_path = find_path(graph, node, end, path, visited)
        else:
            current_path = None
    return current_path


'''
The above function can be easily
extended to find all the paths.
Just add another list: append all the paths 
while looping through the graph in that.

As a precaution one should keep track of visited:
Visited will allow one not to move in the same
cyclic path over and over again.
'''


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    shortest_len = 100 # or any super high number here
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
                if len(newpath) < shortest_len:
                    shortest_len = len(newpath)


    return paths


'''
shortest length of all paths in the list:
Loop over the list of possible paths: as you append them and keep track of a variable called: shortest_length
then iteratively update them.
'''

def find_shortest_path(paths):
    shortest_len = 100 # or any high number here
    for path in paths:
        if len(path)<shortest_len:
            shortest_len = len(path)
            shortest_path = path
    return shortest_path


'''
The time space complexity of a DFS algorithm is:
O(V+E), V: Number of vertices, E: edges
'''

def dfs(graph,start, goal,path = [],visited=set()):
    # Test graph validity
    assert (len(graph) > 0)
    if start not in visited and not start == goal:
        visited.add(start)
        path = path + [start]

    for neighbour in graph[start]:
        if not neighbour == goal:
            if neighbour not in visited:
                visited.add(neighbour)
                path = path + [neighbour]
                return dfs(graph, neighbour,goal,path,visited)
        else:
            return path + [goal]

#Now lets try to solve the problem using BFS
#queue for poping,visited as set data structure.

def BFS(graph, start,goal):
    visited = set()
    path = []
    queue = []
    if not start==goal:
        if not start in visited:
            path.append(start)
            visited.add(goal)
            queue.append(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append(neighbour)
    return path + [goal]


# if '__name__' == '__main__':
# The graph is here given as a list of edges between all the possible pair nodes in the graph

# Write a function: Input: (edge pair) output: graph of set for each
# check below
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

start = 'A'
end = 'D'
print('Find path:', find_path(graph, start, end))
all_paths = find_all_paths(graph, start, end, path=[])
print('Find all paths:', all_paths)
print('The shortest paths:', find_shortest_path(all_paths))
print ('Path traversal based on DFS',dfs(graph,start,end))
print ('BFS path:',BFS(graph,start,end))

# Driver Code

# Walk the interviewer through the space and time complexity in all of the scenarios above.
# In the above code I am walking through the code everytime for every node I encounter
# Clearly the time complexity is exponentially high. THats why we use DFS
# for time complexity.
