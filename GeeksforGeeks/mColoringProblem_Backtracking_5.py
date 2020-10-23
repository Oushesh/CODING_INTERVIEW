'''
mColoring Problem: Backtracking 5
Intro: mColoring Problem:  A 2D a
'''

'''
Outine me some approaches:

Method1: Naive

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
Question 1: 
'''
