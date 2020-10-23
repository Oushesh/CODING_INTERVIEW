'''
Reference: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
'''

'''
What do we need to build a graph?
1. HOw to store graph in python? --> defaultdict(list)
What is the advantage of using defualtdict?

Walk me through the algorithm of the Breadth First Search.

1. First declare a visisted track of visited nodes.
2. Declare a queue
3. Until queue is not empty:
4. append everything we visited and update the visited trackinge
5. use popping to remove possible queues.
6. For another here you do the goal check.
7. Query all neighbours

Example:
> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        #visited = [False for i in range(len(self.graph))]

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print (g.BFS(2))
