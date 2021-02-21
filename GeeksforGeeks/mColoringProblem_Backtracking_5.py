#Ref: https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/

'''
Given an undirected graph and a number m, determine if the graph
can be coloured with at most m colours such that no two adjacent
vertices of the graph are colored with the same color.
Here coloring of a graph means the assignment of colors to all vertices.
'''

'''
Outine me some approaches:

Method 1: Naive

Naive Approach: Generate all possible configurations of colours.
Since each node can be coloured using any of the m available colours,
the total number of colour configurations possible m^V.

After generating a configuration of colour, check if the adjacent
vertices have the same colour or not. THen eliminate the condition.

If conditions are met, print the combination and break the loop.
'''


'''
Method 2: Backtracking

Approach: The idea is to assign colours one by one to different vertices,
starting from index 0. Before assigning a color, check for safety by considering
already assigned colors to the adjacent vertices i.e. check if the adjacent
vertices do not have the same color)

If there is any color assignment that does not violate the conditions, mark the
color assignment as part of the solution. If no assigment of color is possible
then backtrack and return false.
'''


'''
Rephrasing the Question:

No 2 adjacent members should have the same colour:

Lets simplify the question:

A->A (False)
A->B  (True)
A->C  (True)
A->D  (True)


A B C D
1 2 3 2
Here its simple. Lets extend then algorithm to something like:

The best way to represent the problem is a predefined graph:
          A
        / \  \
       B   C  D


Represent this problem  as a dictionary:

map = {'A':['B','C','D']}


Lets invent a more interesting question:
Australia coloring problem:
'''

#TODO: implement a real constraint solver.
