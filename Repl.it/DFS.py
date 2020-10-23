#Cold Blodded DFS writing capabilies
#DFS Algorithm in Python
#DFS : graph declared dict of lists or dict of sets


def dfs(graph,start,visited=None):
    if visited is None:
        visited = set () #you can also make it a list but set has better time complexity: O(1)
    visited.add(start)
    #print (start)

    for neighbours in graph[start] - visited:
        dfs(graph, neighbours, visited)
    return visited

if __name__ == "__main__":
    graph = {'0':set(['1','2']),
             '1':set(['0','3','4']),
             '2':set(['0']),
             '3':set(['1']),
             '4':set(['2','3'])}
    print (dfs(graph,'0'))
