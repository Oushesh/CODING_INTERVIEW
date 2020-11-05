#Reference :
'''
start word: 'dog'
end word: 'hat'

dictionary = ['dot', 'cat','hot','hog','eat','dug','dig']
'''
'''
2 nodes are connected if they differ by 1 letter
# How do we define the difference: letters remain of same length
# Graph algorithm --> Breadth First search
# What is the time complexity? O(V+E)
# V: Vertices, E:Edges

Example:
start: 'dog'
end:   'hat'

# 'dog' -> 'dot' -> 'hot' -> 'hat'
Return true
'''

from queue import Queue

class Node:
    def __init__(self,word):
        self.word = word
        self.neighbors = []

    def addNeighbor(self,neighbor):
        if Node.differeOneLetter(self.word,neighbor.word):
            self.neighbors.append(neighbor)
            neighbor.append(self)

    @staticmethod
    def differeOneLetter(word1,word2): #loop over all the combinations and build pair
        assert(len(word1)==len(word2)) # a must in this problem
        differenes = 0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                differences+=1
            if differences > 1:
                return False
        return True

class Graph:
    def __init__(self):
        self.words = {} #dictionary, neighbours a list {'cat':['dat','car']}
        #differ only by 1 letter

    def addwords(self,word):
        for word in self.words:
            if not word in self.words:
                self.words[word] = Node(word)

    def link(self,word1,word2):
        if word1 in self.words and word2 in self.words:
            self.words[word1].addNeighbor(self.words[word2])

    def BFS(self,start,end):
        if not start in self.words or not end in self.words:
            return False
        #mark all explored nodes at the beginning False
        for word in self.words:
            self.words[word].seen = False

        startNode = self.words[start]
        endNode   = self.words[end]
        q = Queue()
        q.put(startNode)
        #Traverse the tree.
        while not q.empty():
            currentNode = q.get()
            if currentNode == endNode:
                return True #Goal has been reached
            for neighbor in currentNode.neighbors:
                if not neighbor.seen:
                    neighbor.seen = True
                    q.put(neighbor)
        return False

    def isTransformable(self,start,end,dictionary):
        self.addwords(start)
        self.addwords(end)

        for word in dictionary:
            self.addwords(word)
        allNodes = list(self.words.keys())
        for i in range(len(allNodes)):
            for j in range(i+1,len(allNodes)):
                self.link(allNodes[i],allNodes[j])
        return self.BFS(start,end)

#How to make it better?

if __name__ == "__main__":
    dictionary = ['dot','cat','hat','hog','eat','dug','dog']
    g = Graph()
    start = 'dog'
    end   = 'hat'
    print (g.isTransformable('dog','hat',dictionary))
    print (g.isTransformable('dog','ice',dictionary))
