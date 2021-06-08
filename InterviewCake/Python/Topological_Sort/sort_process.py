'''
Reference: https://www.interviewcake.com/concept/java/topological-sort

The following is an undirected graph:

1. The ingredients have to be mixed before going to
bundt pan.

2. The bundt pan has to be greased and floured before
the batter can be poured in.

3. The oven has to be preheated before the cake can bake.

4. The cake has to be baked before it cools.

5. The cake has to cool before it can be iced.

Lets say we have the graph:

Mix Ingredients: Mix
Add Batter to Pan: Batter
Grease/Flour Pan: Grease
Eat Dessert: Dessert
Make Frosting: Frosting
Frost Cake: FC
Cool Cake: Cool
Bake Cake: Bake
Preheat Oven: Preheat
'''

from collections import defaultdict

def make_graph(edges):
    graph = {}
    for edge in edges:
        graph[edge[0]] = edge[1]
    return graph

def topological_sort(graph):
    # Build an in_degrees to know the in_degree of each frame

    in_degrees = {node: 0 for node in graph}  # initialise the node value to 0
    print (in_degrees)

    for node in graph:
        print('node', node)
        for neighbour in graph[node]:
            in_degrees[neighbour] += 1

    return in_degrees


if __name__ == "__main__":
    edges = [['Mix', 'Batt'],
             ['Batt', 'Bake'],
             ['Frosting', 'FC'],
             ['FC', 'D'],
             ['Cool', 'FC'],
             ['BC', 'CC',
              ['PC', 'BC'],
              ['Preheat', 'BC']]]

    graph = make_graph(edges)
    print('graph', graph)

    sorted_graph = topological_sort(graph)
    # print ('sorted_graph',sorted_graph)

# TODO: Test and complete the code.
# Next step extend Topological sorting idea to other problems.
# Complete and nail all coding interview problems. 4 USA
