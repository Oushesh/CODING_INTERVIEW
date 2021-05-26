#Geeks for Geeks
#Ref: https://www.geeksforgeeks.org/python-program-for-topological-sorting/

from collections import defaultdict


'''
1. Take in words buid in a dictionary for words 2 integers.
2. For pair numbers in the integer list
3. Build an adjacncy matrix from the words
4. Perform Topoological Sort.
5. TODO: rewrite with depth, then perform topological sort
   --> get the answer back to integers
'''

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,U,V):
        self.graph[u].append(v)

    def topological_util(self,v,visited,stack):
        visited[i]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.topological_util(i,visited,stack)

    def topologicalsort(self):
        visited = [0]*self.V
        stack = []
        for  i in range(self.V):
            if visited[i]==False:
                self.topological_util(i,visited,stack)

def word2dict(words):
    dict = {}
    i=0
    for word in words:
        for ch in word:
            if ch not in dict:
                i+=1
                dict[ch]=i
    return dict

def words2Graph(words):
    
    dictionary = word2dict(words)
    print ('dictionary',dictionary)
    print (words[0][0])
    g = Graph(dictionary[words[0][0]])
    for i in range(len(words)):
        for j in range(len(words[i])-1):
            print (words[i][j], words[i][j+1])
            g.addEdge(dictionary[words[i][j]],dictionary[i][j+1])
    g.topologicalsort()
    return None

if __name__ == "__main__":
    words = ['wrt','wrf','er','ett','rftt']
    print (word2dict(words))
    words2Graph(words)
