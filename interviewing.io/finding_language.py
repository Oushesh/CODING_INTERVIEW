'''
Reference: https://start.interviewing.io/interview/Igkh0j20Psfa/replay
// Input:  words[] = ["pbb", "bpku", "bpkb", "kbp", "kbu"]
// Output: ['p', 'u', 'b', 'k']
'''


'''
Further Improvement Questions:
How would you design your solution to handle
this case?

Input: ['a', 'b', 'c', 'cd', 'ce', 'cf']
Output: [['a', 'b', 'c'], ['d', 'e', 'f']]

a->b->c                
c->d
c->e
c->f


                          a
                        /    \
                      b         c
                             /     \    \
                            d       e    f

1. Build graph
2. Topological Sort on it Based on DFS                                                  
3. Modify the DFS with ans parameter --> append the answer/path all the way.
   This is the path for the sort algorithm. 
'''
from collections import defaultdict
def dfs(graph,node,visited,ans):
    if node in visited:
        return visited[node]

def topological_sort(words):
    graph = defaultdict(set)
    ans = []
    visited = {}
    for word1,word2 in zip(input,input[1:]):
        for c1,c2 in zip(word1,word2):
            if not c1==c2:
                graph[c2].add(c1)
                break
    print (graph)


if __name__ == "__main__":
    input = ['a','b','c','cd','ce','cf']

    #Graph =
    topological_sort(input)





