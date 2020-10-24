'''
Given the data structure in List of List or 2D Map;
we rewrite it into a graph (dict) datastructure of
adjaceny elements
W

1. map2graph. How to define adjacency pairs? --> if ()

'''

class Islands_Graphs():
        def __init__(self,grid):
            self.grid = grid

        def graph2dict(grid):
            graph = {}
            length = len(grid)
            if not  length> 0:
                raise Error('Length does not exist') #only put when the interviewer asks for edge cases
            width = len(grid[0])
            for i in range(length):
                for j in range(width):
                    if i==0:
                        if j==0:
                            neighbours = [grid[i][j+1],grid[i+1][j]]
                        neighbours = [grid[i][j-1],grid[i+1][j],grid[i][j+1]]
                    elif j==0:
                        if i==length-1:
                            neighbours = [grid[i-1][j],grid[i][j+1]]
                        neighbours = [grid[i][j+1],grid[i+1][j],grid[i-1][j]]
                    elif i==length-1:
                        if j==width-1:
                            neighbours = [grid[i-1][j],grid[i][j-1]]
                        neighbours = [grid[i-1][j],grid[i][j-1],grid[i][j+1]]
                    elif j==width-1:
                        neighbours = [grid[i+1][j],grid[i-1][j],grid[i][j-1]]
                    else:
                        neighbours = [grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]]
                    graph[grid[i][j]] = set(neighbours)  #dict of sets
            return graph

        def dfs(graph,start, visited):
            #Write classical DFS here
            if visited is None:
                visited = set()
            visited.add(start)

            for neighbours in graph[start]-visited:
                dfs(graph, neighbours, visited)
            return visited



if __name__ == '__main__':
    grid = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12']]
    #Build adjacency graph

    print ('The graph of the grid is:')
    print (Islands_Graphs.graph2dict(grid))
