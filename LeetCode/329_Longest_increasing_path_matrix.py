'''
#https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


My approach would be a DFS and condition of building the graph.

Condition of building the Graph.
1. Neighbours (up,down,left,right only), boundary neglected.
2. if neighbour > current_node --> less or equal to neglected.
3. Traverse the graph --> 1 sequennce only --> DFS would work. No BFS
'''

from collections import defaultdict

def min_matrix_idx(matrix):
    min = 10000 #some big number
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]<min:
                min=matrix[i][j]
    return i,j


def make_graph(matrix):
    graph = defaultdict(list)
    visited = {}
    neighbours = [(-1,0),(1,0),(0,-1),(0,1)]  # 4 neighbourhood

    #A different loop
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for neighbour in neighbours:
                nx = (neighbour[0]+i)
                ny = (neighbour[1]+j)
                if nx >= len(matrix) or ny >= len(matrix[0]) or nx < 0 and ny < 0:
                    continue
                if matrix[nx][ny] > matrix[i][j] and matrix[i][j] not in visited:
                    graph[matrix[i][j]].append(matrix[nx][ny])

    return graph


'''
AIM here is to it:
Recursive: keep track of arguments
'''
def dfs(graph,start,path,path_length):
    
    return dfs(graph,curr_node,path,path_length)

'''
Approach 1: 
Questions to clarify with the interviewer:
1. Is the start given? If yes, use it else, use min(graph)
2. If not told what kind of neighbourhood do we need? 4-neighbourhood or 8-neighbourhood?
3. Clarify travel inside the boundary.

Then:
perform dfs here. 
'''

if __name__ == "__main__":
    matrix = [[1,2,3],[5,6,9],[10,12,11]]
    min_x,min_y = min_matrix_idx(matrix)
    graph = make_graph(matrix)
    print ('graph',graph)
    #dfs(graph,start)