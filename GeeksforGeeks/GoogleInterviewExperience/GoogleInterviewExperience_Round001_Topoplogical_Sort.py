###Reference: https://www.geeksforgeeks.org/google-interview-experience-on-site-for-sde/

'''
Google Interview Experience | On-Site for SDE
Difficulty Level: Hard

Round 1: There are several equations given in terms of 2 variables
with a '<' or '>' sign between them. Ex-a>b, b>c etc...
You have to answer whether there is a sequence which of the
variables which will satisfy all the equations given.

Ans: Maybe its topological sorting.
A group of inequalities here and there.

Then we have to standardise the symbols.

a>b>c

From the conditions given build a graph? Check for
contradiction --> a>b b>a

a>b>c a->b
a>b>d a->b
b->d>e b->d, c,d unknown-> there is unless there is a direct contradiction.
d>b
How do we model this problem? Graph a->b: graph = {a:b}
1. I cannot sort this out. Completely.
   unless all the equations in the first one appear
   the second one in the inquality equation lineup.
   That is: if a,b are the same: take it.

abc a->b
abd
cd -> cd

e:  Constraint: if we have only 1 element: Constraint.

abcde
abde
abc
abd
compare elementwise: if elments the same: then build the graph.
if not break.

'''

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
from collections import deque

class Solution:
    def inequalities_order(self, equations):
        # Build a graph from adjacency list and indegrees graph
        # Perform Traversal. Lets do this time:BFS --> O8V+E)

        adjList = {}
        # unique alphabets here:
        variables = set([var for equation in equations for var in equation])
        indegrees = {node: 0 for node in variables}
        print (indegrees)

        for equation in equations:
            for var in equation:
                if var not in adjList:
                    adjList[var]= set()


        #Loop in the equations:
        for i in range(1,len(equations)):
            first_eq = equations[i-1]
            second_eq = equations[i]
            length = min(len(first_eq),len(second_eq))
            for i in range(length):
                if not first_eq[i]==second_eq[i]:
                    adjList[second_eq].add(first_eq)
                    indegrees[first_eq]+=1
                    break

        output = []
        queue = deque([var for var in adjList if indegrees[var]==0])

        #Build a queue
        while queue:
            node = queue.popleft()
            output.append(node)
            for neighbour in adjList[node]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour]==0:
                    queue.append(neighbour)


        #Test result:
        return output if len(output)==len(adjList) else ''

if __name__ == "__main__":
    input = ['a', 'b', 'c', 'cd', 'ce', 'cf']
    current_Sol = Solution()
    print('The current order is:', current_Sol.inequalities_order(input))
