'''
Topological Sort:
A classical approach.

1. Build the graph.
2. Get the incoming edges degree.
3. Identify node with no incoming edges
4. Remove that node from graph or mark it.
5. Repeat: len(directed graph) == len(given graph) -->
   otherwise Cyclic property --> Graph cannot be converted to Topological Graph

Problem of finding alien dictionary:
'''

from collections import defaultdict

def make_graph(words):
    graph = defaultdict(set)
    for word1,word2 in zip(words,words[1:]):
        for ch1,ch2 in zip(word1,word2):
            if ch1!=ch2:
                graph[ch2].add(ch1)
            #graph[ch1].add(ch2)
    return graph

def topological_sort(graph):
    # Get incoming degrees
    in_degrees = {node: 0 for node in graph}
    print (in_degrees)
    for node in graph:
        for neighbour in graph[node]:
            in_degrees[neighbour]+=1
    print (in_degrees)
    # Track node with no incoming edges.
    no_incoming = []
    for node in graph:
        if indegrees[node]==0:
            no_incoming.append(node)

    # Set node with no_incoming edge as root node
    queue = []
    while len(queue)>0:
        current_node = no_incoming.pop()
        queue.append(current_node)
        for neighbour in graph[current_node]:
            indegrees[neighbour]-=1
            if indegrees[neighbour]==0:
                no_incoming.append(neighbour)
    return queue

if __name__ == '__main__':
    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    word_graph = make_graph(words)
    print ('The graph is:',make_graph(words))
    topological_order = topological_sort(word_graph)
    print ('The order is:',topological_order)





