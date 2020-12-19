#Oushesh haradhun
'''
We translate the rules of the game to graph connectedness.
blocks we have = 10
1) Moving from currrent block to the neighbour require a difference of <=1
    abs(game[x][y]-game[i][j]<=1)
    loop over all the neighbours.

    Write a function(x,y):
             call the neighbours and check connectedness
             Connectedness:
             At each step from 1 neighbour to the other we
             might have 2 choices. either 'p' or 'n'
             At each node I need to track: (b:10)
             If both possible
'''
class Game():
    def __init__(self):
        block = self.block
        direction = self.direction
        start = self.start
        end   = self.end
    '''
    We build a dictionary of lists:
    The list contains important information like:
    block value, parent block, child_current_block, boolean visited or not
    How does it look?: dict[(x,y)]= [block value, parent block, child_current_blocks, boolean_vistied]
    pg represents playground
    '''
    def visited(self,pg):
        '''
        visited: dict initialised with 0
        if 1: visited, 0: not visited
        '''
        visited = {}
        for x in range(len(pg)):
            for y in range(len(pg)[0]):
                visited[(x,y)]=0
        return visited

    def neighbours(self,x,y,visited,playground):
        '''
        In this function each time we have an x,y coordinate
        we build the neighbour
        '''
        neighbours = [(x+1,y),(x-1,y),(x,y+1),(x,y-1) if x>=0 or x<len(playground) or y>=0 or y<len(playground[0])]
        return neighbours

    '''
    Direction_check takes in direction and aligns the direction
    properly
    '''
    def direction_check(self,direction,start,goal,output):
        #Check if given instruction for direction aligns with goal direction
        #Define pos_x,pos_y
        #If alignment is true, return True.
        #else: correct alignement and update the output instruction
        if end[0] > start[0]:
            #positive_x
            pos_x = True
        else:
            pos_x = False

        if end[1] > start[1]:
            pos_y = True
        else:
            pos_y = False

        #Make direction alignment
        if pos_x and direction=='r':
            return output

        if not pos_x and direction=='l':
            return output

        #now let's do the alignment
        if not pos_x and direction=='r':
            #move 2 times
            output.append('r')
            output.append('r')
            return output
        return output

    def connectivity(self,node,visited,playground,output):
        '''
        node=(x,y), node[0],node[1]
        Connectivity takes in the current node gets the
        neighbours from function neighbour. For each neighbour, we
        check the connectivity and update its visit attribute
        in the graph given.
        '''

        neighbours = self.neighbours(node[0],node[1],visited,playground)
        #Call the function to initialise visited map
        visited = self.visited(playground)
        if not visited[(x,y)]:
            #update the visited paremeter here
            visited[(x,y)]=1
            for neighbour in neighbours:
                #check if we can move to the next.
                #playground[x][y]
                if playground[neighbour[0]][neighbour[1]]==-1:
                    #We canot take we can only put
                    #continue putting blocks and always make sure block number >0
                    while (playground[node[0]][node[1]]) and block>0:
                    output.append('p')

                #


        return True, output

    '''
    DFS traversal for the algorithm.
    '''
    def dfs(self,graph,start,visited=None):
        if visited is None:
            visited = set() #
        return visited

    def build_tree(self,playground,start,block):
        '''
        graph={(x,y):[(x_child,y_child),block, parent_value,its value, visited or not]}
        Loop over the playground, check the connectivity.
        If true add the (x,y) as the
        Perform the dummy initialisation here.
        '''
        #initialise the graph here with the correct structure
        #start(x,y)
        playground
        visited_map = self.visited(playground)
        grpah = {start:[None, block, None,playground[x][y]],visited_map[(x,y)]}

        '''
        Loop over every node (x,y), get their neighbours. if sel
        '''
        if self.connectivity():




        return tree

    def main(self,playground,start,goal,direction):
        #assert the start and goal are not the same.
        assert(not start == goal)
        #Make sure the direction points towards the x or y axis of the goal and not opposite
        self.direction_check(direction,start,goal)
        '''
        Second Step is to Build graph
        '''
        self.build_tree(playground,start)
        '''
        Perform DFS to traverse the graph
        '''

        return True
if __name__ == "__main__":
    #Game contains any number from -1 to 10
    blocks = 10
    height  = 6
    '''
    Instructions contain: r: right (clockwise rot), l:left (anticlockwise rot),s: step,
    p: put block onto the field
    n: take block from the field
    '''
    instructions = ['r','l','p','s','n']
    #output for the instructions to be appended
    output = []

    #lets say 5x5
    start = (0,0)
    end   = (5,3)

    #we also build a way to track whether we visited or not
    playground = [[1,2,4,5,6],[-1,3,5,6,7],[1,1,-1,3,4],[4,3,5,7,9],[2,3,5,7,9]]
    direction =
    #initialise the class here
    Game()
    print ('The visited map is:',Game.visit_map())
