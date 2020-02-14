#2.5 years Experience

#start: 'dog'
#end: 'hat'

#dictionary = ['dot','cat', 'hot','hog','eat','dug','dig']


#In each step its about changing one letter until I reach the goal.
# Graph problem

#How do I define my problem?
#start word:'dog'
#Goal word: 'hat'


#Bidirectional  breadth first search.
#cuts the runtime down. HOw do we tackle the problem of visited nodes?

dictionary = ['dot','cat','hot','hog','eat','dug','dig']

#Write your thought:
#. Two nodes are connected if they differ by 1 letter
#1. Assume single letter replacement
#2. Graph Algorithm --> Breadth First Search
#3. Runtime O(V+E): where V is the number of vertices and E: edges
#Can we do better?


#Can we do better?
#Bidirectional Search ??

from queue import Queue

#'dog' -> 'dot' -> 'hot' -> 'hat'
class Node:
    def __init__(self,word):
        self.word = word
        self.neighbors = []

    def addNeighbor(self,neighbor):
        if self.differbyOneLetter(self.word,neighbor.word):
            self.neighbors.append(neighbor)
            neighbor.append(self)

    def differOneLetter(word1,word2):
        assert(len(word1)==len(word2))
        differences  = 0
        for i in range(len(word1)):
            if word[i]!=word2[i]:
                differences+=1
                #we are assuming that the letters in our case have max. difference of 1.
            if differences > 1:
                return False
            return True


class WordGraph:
    def __init__(self):
        self.words = {}


    def addWords(self,words):
        if not word in self.words:
            self.words[word]=Node(word)

    def linkWords(self,word1,word2):
        if word1 in self.words and word2 in self.words:
            self.words.addNeighbor(self.words[word2])


    #We define the Breadth First algorithm:
    #takes in node, start word and destination
    def BFS(self,start,end):
        if not start in self.words or not end in self.words:
            return False
        #Keep track of viisted Node
        for word in self.words:
            self.words[word].seen = False
        #else: check all the traversed ones until one
        #perform goal check
        startNode = self.words[start]
        #stack all the frontiers
        q1 = Queue()
        q1.put(startNode)
        endNode  = self.words[end]
        q2 = Queue()
        q2.put(endNode)
        while not q1.empty():
            current = q1.get()
            #Perform goal check
            if current == endNode:
                return True
            for neighbour in current.neighbors:
                if not neighbor.seen:
                    neighbour.seen = True
                    q1.put(neighbor)
        return False

    def isTransformable(self, start,end, dictionary):
        self.addWords(start)
        self.addWords(end)

        for word in dictionary:
            self.addWords(word)
        allNodes = list(self.words.keys())
        for i in range(len(allNodes)):
            for j in range(i+1,len(allNodes)):
                self.linkWords(allNodes[i],allNodes[j])
        return self.BFS(start,end)

#Testing here:

if __name__ == '__main__':
    dictionary = ['dot','cat','hot','hog','eat','dug','dig']
    g = WordGraph()
    assert(g.isTransformable('dog','hat',dictionary))
    assert(not g.isTransformable('dog','ice', dictionary))
