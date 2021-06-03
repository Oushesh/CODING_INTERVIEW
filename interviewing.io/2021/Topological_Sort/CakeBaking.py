'''
Given constraints:
build directed graph.
1. Mix Ingredients,M --> Add to Batter pan, B
2. Grease/Floor Pan,G --> Add to Batter pan, BP
3. Preheat Oven,P --> Bake Cake,BC
4. Add Batter Pan,BP --> Bake Cake,BC --> Cool Cake, CC
5. Cool Cake,CC --> Frost Cake,FC
6. Frost Cake,FC --> Eat Dessert,D
7. Make Frosting,MF --> Frost Cake,FC

#Reference: InterviewCake: https://www.interviewcake.com/concept/python3/topological-sort
'''

from collections import defaultdict
# The conditions are like edges: of a graph


def conditions2graph(conditions,graph):
  for condition in conditions:
    u = condition[0]
    v = condition[1]
    #assert (not u==v)
    graph[v].add(u)
  return graph

# Topological Sort Algorithm.
# Method 1: Do depth first search
# Method 2: 1. Calculate in_degrees of each node
#           2. Perform walk for nodes with zero and their neightbours: decrease the count.
#           3. In the process append the path # as output.
def topological_sort(conditions,states):
  #initialiase in_degrees with 0.
  in_degrees = {node:0 for node in states}
  for node in states:
    for neighbour in graph[node]:
      in_degrees[node]+=1

  print ('in_degrees',in_degrees) #till here all good.
  #now we have the indegrees.
  #Get all the starting nodes
  #:nodes with 0 indegrees
  starting_nodes = []
  print ('states',states)
  for node in states:
    if in_degrees[node]==0:
      starting_nodes.append(node)

  #Until starting_nodes, all good and debugged
  print ('starting_nodes',starting_nodes)

  #Now start the topoological sort:
  output = []
  while (len(starting_nodes)>0):
    current_node = starting_nodes.pop()
    output.append(current_node)
    print ('output',output)
    for neighbour in graph[current_node]:
      #Decrease in_degrees connectivity:
      print ('neighbour of starting',neighbour)
      in_degrees[neighbour]-=1
      if in_degrees[neighbour]==0:
        starting_nodes.append(neighbour)


  #we've run out of nodes with no incoming
  #edges. 2 possibilities
  # Cyclic Graph: we cannot decompose this graph

  '''
  in simple words, the number of edges coming towards a vertex(v) in Directed graphs is the degree of v.
  '''

  print (output)
  if len(graph)==len(output):
    return output
  else:
    raise Exception('Graph has a cycle')

#if '__name__' == '__main__':
states = ['M','BP','G','P','BC','CC','FC','D','MF']


conditions = {'M':'BP','G':'BP','P':'BC','BP':'BC','BC':'CC','CC':'FC','FC':'D','MF':'FC'}
graph = defaultdict(set)
#conditions_graph = conditions2graph(conditions,graph)
#print ('conditions_graph:',conditions_graph)

sorted_graph = topological_sort(conditions,states)
print ('sorted_graph',sorted_graph)

#TODO: test the states here get all the state #--> all the states here and there do not have
#any error.
#TODO: error is in the way of building the graph.
