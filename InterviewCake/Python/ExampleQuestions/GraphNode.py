#Reference: https://www.interviewcake.com/question/python3/graph-coloring?utm_source=weekly_email&utm_source=drip&utm_campaign=weekly_email&utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23288:%20Reverse%20Words&utm_medium=email&utm_medium=email&__s=ap5rqqpkspoovezbmxvs

'''
Given an undirected graph with maximum degree
D, find a graph coloring using at most D+1
colors.


This graph's maximum degree (D) is 3, so we
have 4 colors (D+1). Here's one possible
coloring.

Graphs are represented by a list of N node objects,
each with a label, a set of neighbors, and a color:
'''

'''
Does your function go through every color for every ndoe?
Not needed. We can do better. You don't want N*D in your final
runtime.
Brute Force would for instance would lead to: D^N.
'''

class GraphNode:
    def __init__(self,label):
        self.label     = label
        self.neighbors = set() #thats a good choice
        self.color     = None


    def 
'''
Graph Building
'''

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a,b,c]
