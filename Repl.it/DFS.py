#Cold Blodded DFS writing capabilies
#DFS Algorithm in Python
#DFS : graph declared dict of lists or dict of sets

#recursive implementation
def dfs(graph,start,visited=None):
    if visited is None:
        visited = set () #you can also make it a list but set has better time complexity: O(1)
    visited.add(start)
    #print (start)
    for neighbours in graph[start] - visited:
        dfs(graph, neighbours, visited)
    return visited

'''
Iterative implementation of Depth First search.
How do we define graph? -->
'''

def dfs_iterative(graph,start):
    stack, path = [start], [] #we wrap the data into empty set to perform list operation of addition
    while stack:
        current_node = stack.pop()

        if current_node in path:
            continue
        path.append(current_node)
        for neighbour in graph[current_node]:
            stack.append(neighbour)
    return path

'''
Tweak the idea for path generation using recursive implementation,

'''

def dfs_path(graph,start,goal,visited=None,path=None):
    return None

if __name__ == "__main__":
    graph = {'0':set(['1','2']),
             '1':set(['0','3','4']),
             '2':set(['0']),
             '3':set(['1']),
             '4':set(['2','3'])}
    print ('recursive approach',dfs(graph,'0'))

    #Implementtion of iterative path

    graph2 = {'0':['1','2'],
             '1':['0','3','4'],
             '2':['0'],
             '3':['1'],
             '4':['2','3']}
    print ('iterative approach',dfs_iterative(graph2,'0'))
