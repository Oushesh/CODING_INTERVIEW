#Breadth First Search
#Cold implementation and check how does it work

'''
Pseudo Code:

create a Queue Q
mark v as visited
put v into Q

while Q not empty:
    remove the head u of Q
    mark and enqueue all (unvisited) neighbours of u
'''

'''
Why use dequeues over lists? --> dequeues are more efficient than lists
specially if you always remove the last or first element (pop_left,pop) vs
lists of O(n) time complexity
'''

import collections
from collections import deque

#DFS Algorithm
def BFS(graph, root):
    visited = set()
    queue   = deque([root])
    visited.add(root)

    while queue:
        #Dequque a vertex from Queue
        vertex = queue.popleft()
        print (str(vertex) + " ", end=" ")

        #if not visited, mark as visited and
        #enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                #for set we use add, for list we use append
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    graph = {0:[1,2], 1:[2],2:[3],3:[1,2]}
    print ('Following is Breadth First Traversal:')
    BFS(graph,0)
