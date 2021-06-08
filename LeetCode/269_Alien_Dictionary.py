'''
This is an example of Topoological Sorting.
https://www.youtube.com/watch?v=fhCXVABhFDc
'''

'''
Lets take a simple example: 
How do we move around this? 
[
 Za,    --> From this pair we conclude a->b 
 zb,      z-> c
 ca,  --> a -->b 
 cb   --> z-->c
 
 All possible combinations here: 
 we have all possible alphabets: 
 set() for c in word for word in words
 
 We can build all combinations here: 
 indegrees = {node:0 for node in graph}      
]

The only 2 information I can extract from here is: 
We always compare the elements: once its not the same -_> we create 
an edge for a 
'''

from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        # Build a graph from adjacency list and indegrees graph
        # Perform Traversal. Lets do this time:BFS --> O8V+E)

        adjList = {}
        # unique alphabets here:
        alphabets = set([c for word in words for c in word])
        indegrees = {node: 0 for node in alphabets}
        print(indegrees)
        # One Line Command:
        # adjList = [default(set) for c in word for word in words if c not in adjlist]

        # Classical Way

        for word in words:
            for c in word:
                if c not in adjList:
                    adjList[c] = set()

        # Loop in the words: each time it does not match--> I have an edge
        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]
            # now we have 2 length:
            length = min(len(first), len(second))
            # now I do pairwise looping
            for i in range(length):
                if not first[i] == second[i]:
                    CharIn = first[i]
                    CharOut = second[i]
                    if first[i] not in adjList:
                        # Build the edge here:
                        adjList[CharOut].add(CharIn)
                        indegrees[CharIn] += 1
                    break

        result = ''
        queue = deque([c for c in adjList if indegrees[c] == 0])

        # now I perform a BFS and queue the elements whose indegrees is 0:
        while queue:
            c = queue.popleft()
            result += c  # store the path of the correct order.
            for neighbour in adjList[c]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    queue.append(neighbour)

        # Here at the end I am gonna the result
        # the end result is not the same as len(adjList)--> cylic graph --> invalid
        return result if len(result) == len(adjList) else ''


if __name__ == "__main__":
    input = ['a', 'b', 'c', 'cd', 'ce', 'cf']
    current_Sol = Solution()
    print('The current order is:', current_Sol.alienOrder(input))
