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

def make_graph():
    return graph

def topoological_sort(graph):
    return sorted_graph

if __name__ == "__main__":
    edges = [['Mix','Batt'],['Batt','Bake'],['Frosting','FC'],['FC','D'],[]]
    graph = make_graph(edges)
    sorted_graph = topoological_sort(graph)


#TODO: Test and complete the code.
#Next step extend Topological sorting idea to other problems.