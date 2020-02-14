#Ideas Steps:
#Loop over word
#initialze the start at i,
#anchor to be determined. if s[i:J] in Dict;
#add s[i:j] in expored_set
#the other part: s[j+1:n]
#Breadth First Search Algorithm
#check the other: if other in Dict; return Breakable=True
from queue import Queue
import collections
class Solution_BFS:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Modeled as a graph problem - every index is a vertex
        #and every edge is a completed word
        # The problem thus boils down to if a path exists.
        queue = collections.deque()
        visited = []
        queue.appendleft(0)
        visited.append(0)
        while len(queue) > 0: #queue is not empty
            curr_index = queue.pop()
            for i in range(curr_index, len(s)+1):
                if i in visited:
                    continue
                if s[curr_index:i] in wordDict:
                    if i == len(s):
                        return True
                    queue.appendleft(i)
                    visited.append(i)
        return False

#Time Complexity: O(V+E) O(n²),
#Space Complexity: O(n)
class Solution_DFS:
    def wordBreak(self,s,wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        queue = [] #using Default list to implement stack
        visited = []
        queue.append(0)
        visited.append(0)
        while len(queue)>0:
            curr_index = queue.pop()
            for i in range(curr_index,len(s)+1):
                if i in visited:
                    continue
                if s[curr_index:i] in wordDict:
                    if i==len(s):
                        return True
                    queue.append(i)
                    visited.append(i)
        return False


#Different Version of Dynamic Programming
#For the approach of Dynamic Programming:
#move 2 indices i,j
#j<i
class Solution_Dynamic_Programming:
    def wordbreak_DP(self,s:str, words)->bool:
        cut = {0: True}
        for i in range(1,len(s)+1):
            cut[i] = False
            for j in range(i):
                if cut[j] and s[j:i] in words:
                    cut[i] = True
                    break
        return cut[len(s)]

if __name__  == '__main__':
    s = 'catsanddog'
    wordDict = ["cats", "dog", "and", "cat"]
    output = Solution_Dynamic_Programming()
    print ('Dynamic Programming solution:')
    print ('Is the Word Breakable?:',output.wordbreak_DP(s,wordDict))

    BFS_output = Solution_BFS()
    print ('Breadth First Search Solution:')
    print ('Is the word Breakable?:',BFS_output.wordBreak(s,wordDict))


    DFS_output = Solution_DFS()
    print ('Depth First Search Solution:')
    print ('Is the word Breakable?:',DFS_output.wordBreak(s,wordDict))
