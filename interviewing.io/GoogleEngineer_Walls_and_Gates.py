'''
Leetcode Link: https://leetcode.com/discuss/interview-question/algorithms/124722/facebook-phone-screen-walls-and-gates
Interviewing.io Link: https://interviewing.io/recordings/Java-Google-22
Asked at Facebook Phone Screen interview. Can also be asked at Google
Phone Screen Interview
'''

'''
Description:
inf - parking lots
0 - cars
-1 - obstacle
Space 2D Array:
4x4 matrix
[
 [inf, -1,  0,  inf],
 [inf, inf, inf, -1],
 [inf, -1,  inf, -1],
 [0,   -1,  inf, inf],
]

Desired output:
[
 [3, -1, 0, 1],
 [2, 2, 1, -1],
 [1, -1, 2, 1],
 [0, -1, 3, 4]
]
'''

'''
By the way peeps, if you use, deque.popleft()
its a good thing to tell the interviewer that
its faster than normal list.pop() or list.pop(0)
deque in python has been optimised to to popleft()
approximately in O(1), while list.pop(0) takes
O(n) time (Time Complexity) --> (see deque objects)

Why? Namely that a deque object "is composed of a
doubly-linked list", which effectively optimizes
appends and pops at both ends, while list objects
are not even singly-linked lists but C arrays
(of pointers to elements), which makes them good
for fast random access of elements but requires O(n)
time to reposition all elements after removal of the
first.
'''


import collections
from collections import deque

#Other approach
#then the BFS approach.
#facebook coding interview
#facebook,
class ParkingSpace():
    def cost_space(self,rooms):
        #write the condition for the boundaries to
        m = len(rooms)
        n = len(rooms[0])
        if not rooms or not m or not n:
            return None

        for x in range(m):
            for y in range(n):
                if rooms[x][y]==0:
                    #as a rule of thumb if you think
                    #about solving a problem in a recursive
                    #way and you need to know the variables to pass in,
                    #always pass in variables that will get updated
                    self.dfs(rooms,x,y,0)
        return rooms
    #the updating dfs function
    def dfs(self,rooms,x,y,distance):
        #take care of the edge cases and the lookout for error out
        #of boundary terms
        m = len(rooms)
        n = len(rooms[0])
        if (x<0 or y<0 or x>=m or y>=n or rooms[x][y]<distance):
            return None
        rooms[x][y] = distance
        #Perform 4 neighbourhood check
        # left,right, up, down
        self.dfs(rooms,x,y-1,distance+1)
        self.dfs(rooms,x,y+1,distance+1)
        self.dfs(rooms,x-1,y,distance+1)
        self.dfs(rooms,x+1,y,distance+1)
        #return the updated room map
        return None

class WallsAndGates():
    def dfs(self, x,y,dis,directions,rooms):
        row = len(rooms)
        col = len(rooms[0])
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<row and 0<=ny<col and rooms[nx][ny]>rooms[x][y]:
                rooms[nx][ny]=dis+1
                self.dfs(nx,ny,dis+1,directions,rooms)
        return None

    def wallsAndGates(self,rooms):
            """
            Do not return anything, modify rooms in-place instead.
            """
            if not rooms:
                return []
            row = len(rooms)
            col = len(rooms[0])
            directions=[(-1,0),(0,1),(1,0),(0,-1)]

            for x in range(row):
                for y in range(col):
                    if rooms[x][y] == 0:
                        self.dfs(x,y,0,directions,rooms)
            return space

'''
Change the strategy to BFS.
1. check for edge cases
2. We still start at room[x][y]==0
'''
class WallsAndGates_BFS():
    def wallsAndGates(self,rooms):
        row = len(rooms)
        col = len(rooms[0])
        distance = 0
        #check whether rooms exist or not
        if not rooms or not len(rooms[0]):
            return None

        #define stack:
        stack = collections.deque()
        for x in range(row):
            for y in range(col):
                if rooms[x][y] == 0:
                    stack.append([x,y])
        neighbours = [(-1,0),(1,0),(0,-1),(0,1)]
        while stack:
            #pop stack
            (x,y) = stack.popleft()
            for (i,j) in neighbours:
                nx, ny = x+i, y+j
                if 0<=nx<row and 0<=ny<col:
                    if rooms[nx][ny]== float("Inf"):
                        stack.append([nx,ny])
                        rooms[nx][ny] = distance
        return rooms

'''
The last approach is the elegant approahch:
we convert the whole datastructure to a graph and then pass
in the BFS code inside it.

The idea here is to build a a graph based on neighbourhood
condition like preferred. We use the 4 neighbourhood defacto
to help us define neighbours.
'''

class WallAndGates_BFSElegant():
    def room2graph(self,rooms):
        '''
        Loop over all the coordinate cells.
        Build the negibourhood mechanism
        then append it as neighbours
        '''
        graph = {}
        neighbours = [(-1,0),(1,0),(0,-1),(0,1)]
        row = len(rooms)
        col = len(rooms[0])

        for x in range(len(row)):
            for y in range(len(col)):
                current_neighbours = []
                for (i,j) in neighbours:
                    nx, ny = x+i, y+i
                    current_neighbours.append((nx,ny))
                    if 0<=nx<row and 0<=ny<col:
                        #Build the neighbours for each nx,ny
                        graph[(x,y)] =  set(current_neighbours)
        return graph

    def WallsAndGates(self,rooms):
        #check first if room exist
        row = len(rooms)
        col = len(rooms[0])

        if not row or not col:
            break

        for i in range(row):
            for j in range(col):


    def BFS(self,graph):
        '''
        Graph traversal of BFS here
        '''
        return visited


if __name__ == '__main__':
    space = [
             [float("Inf"),  -1 , 0 , float("Inf")],
    		 [float("Inf"), float("Inf") ,float("Inf"),  -1],
    		 [float("Inf"),  -1 ,float("Inf"),  -1],
      		 [0,  -1, float("Inf"), float("Inf")]
             ]
    current_parking_space = WallsAndGates()
    print ('The resulting cost space is:',current_parking_space.wallsAndGates(space))

    current_space = ParkingSpace()
    print ('The resulting cost space is using a recursive call is:',current_space.cost_space(space))

    current_space_BFS = WallsAndGates_BFS()
    print ('The resulting cost space using BFS is the following:',current_space_BFS.wallsAndGates(space))
