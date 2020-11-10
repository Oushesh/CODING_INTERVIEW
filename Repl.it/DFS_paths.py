'''
An exercise to generate the paths by tweaking the original
DFS algorithm with minimum changes so one
can easily replicate or remember it when it has
to be used to solve massively complex problems.

iisting vs generator.
Reference to learn: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
'''
import math

class Generic_Problem():
    def DFS_path(self,graph,start,goal):
        '''
        return of all possible paths
        Here we use a list of lists for the
        with the first as current node and
        the other one is
        '''
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                #check if goal is reached
                if next == goal:
                    yield  path + [next] #build the path
                else:
                    stack.append((next, path + [next]))
        return None

    def shortest_path_neat(self,generated_paths):
        '''
        use of lambda expression where:
        '''
        return min(generated_paths, key=lambda path:len(path))

    def shortest_path(self,generated_paths):
        '''
        generated_paths: list of lists
        based on the length of list
        '''
        min_length = math.inf
        for path in generated_paths:
            if len(path) < min_length:
                min_length = len(path)
                shortest_path = path
        return shortest_path

    def path_exist(self,generated_paths):
        '''
        Boolean saying whether path exists or not.
        '''
        if len(generated_paths)==0:
            return False
        return True

if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
         'B': set(['A','D','E']),
         'C': set(['A','F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    current_graph = Generic_Problem()
    #The path is actually as a list of list:
    generated_paths = list(current_graph.DFS_path(graph,'A','C'))
    print ('All the possible paths are as following:',generated_paths)
    print ('The shortest path',current_graph.shortest_path(generated_paths))
    print ('The shortest path based on lambda expression structure',current_graph.shortest_path_neat(generated_paths))
    print ('There exists a path between start node and goal node:',current_graph.path_exist(generated_paths))
