'''
This type of writing the topological
sort is based on youtube video from here:
https://www.youtube.com/watch?v=guJkbg-gnLM
'''

'''
Why and when Toopological sort?
Why and when -- efficient graph like way to deal with ordering 
of processes where the entities are linked together.


Pseudo Algorithm:

1. Build a graph if not given out of the edge list given
2. Loop over the graph count the in-degree --> (number of
incoming edges at each node)

3. Save all the nodes with 0-indegree first as: starting_nodes = []
4. For all nodes in startging_nodes:
    add to queue.
    while queue not empty:
       go through children (for children in graph[nodes]):
          in_degrees[childres]-=1
          
          if the in_degrees[node]==0
            put in the queue

Here given the words we need to build the pairwise edges:
loop pair --> build graph then test.
'''




if __name__ == "__main__":
    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
