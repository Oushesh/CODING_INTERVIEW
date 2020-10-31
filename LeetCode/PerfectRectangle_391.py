#Reference: https://leetcode.com/problems/perfect-rectangle/

'''
Given N axis-aligned rectangles where N> 0,
determine if they all together form an exact
cover of a rectangular region.
'''

'''
Algorithmic Development:
1. Lets loop over min or max of the whole given Cartesian coordinates
2. fILL THE 2D Array with Os. (initialisation)
3. For each rect in rectangles:
    loop over all the space and update the 0s with 1s if its fulfilled.

4. Build a hashmap (python dict) to keep track of each coordinate whether
   its filled or not. dict = {(0,0):0} for example or 1s

5. Check if cell already has 1s: if yes break

6. Finally, check if Os are present in 2D map dict: if yes break.

7. Like this we checked overlap or emptiness which both lead to being
false.
'''

class Rectangles():
    #Build map and keep track of filled or not --> Hasmap, dict
    def maingraph(self,rectangles):
        #find lowest left and most upper right coordinate
        lowest_left = min(min([rect[0] for rect in rectangles],[rect[1] for rect in rectangles]))
        upper_right = max(max([rect[0] for rect in rectangles],[rect[1] for rect in rectangles]))
        #loop initialise with 0s
        graph = {}
        '''
        So how do we represent the coordinates:
        (1,1) --> (2,3)
        2 - 1 = 1
        3 - 1 = 2

        Then we have 1 in x and 2 in y -->
        Cell keys being: (1,1),(1,)
        '''
        step_x = upper_right[0] - lowest_left[0]
        step_y = upper_right[1] - lowest_left[1]

        #initiaise the graph with the first coordinate
        graph[(lowest_left[0],lowest_left[1])] = 0

        #populate the cell_keys:
        for i in range(step_x):
            for j in range(step_y):
                graph[(lowest_left[0]+i,lowest_left[1]+j)] = 0
        return graph

    def rect_keys(self,rect):
        '''
        we take in single rectangles
        and build a list of keys to
        be fed later on onto the minigraph
        to check for emptiness or fullness of
        each cell:
        rect: [(1,1),(3,3)]
        '''
        '''
        Populate the keys:
        '''
        keys = []

        step_x = rect[1][0] - rect[0][0]
        step_y = rect[1][1] - rect[0][1]
        #keys.append((rect[0][0],rect[0][1]))

        for i in range(step_x):
            for j in range(step_y):
                keys.append((rect[0][0]+i,rect[0][1]+j))
        return keys

    def check_overlap(self,maingraph,rect_keys):
        '''
        rtype: True if empty of false
        key: (1,3) or (2,3)
        maingraph: graph{(1,3):0,(2,3):0}}
        '''
        for key in rect_keys:
            if key in maingraph.keys(): #first check if the key exists --> if the coordinate even exists
                #Then check whether the value of the graph is 0 or 1. O implies empty, 1 implies occupied
                if maingraph[key]==0:
                    #set the cell to explored--> 1
                    maingraph[key]=1
                elif maingraph[key]==1:
                    return True,maingraph #True: overlap
        return False,maingraph

    def check_emptiness(self,maingraph):
        if 0 in maingraph.keys():
            return True #True: empty --> 0s in the keys
        return False #False:

    def complete_check(self,rectangles):
        '''
        1. Take in the list given and build the occupancy grid or map set Os
        2. Take the individual rects and build their individual keys and check for conflict
        3. Only when there is no conflict, then check for emptiness of the main_graph:
            if that gives true then:
        4. overall we have true else False
        '''
        main_graph = self.maingraph(rectangles)
        current_graph = main_graph
        count_check_overlap = 0
        for rect in rectangles:
            print ('rect',rect)
            current_keys = self.rect_keys(rect)
            print ('all keys',current_keys)
            status, current_graph=self.check_overlap(current_graph, current_keys)
            print ('Graph',main_graph)

            #Perform the check_overlap for all rectangles and check the overlap status
            if not self.check_overlap(current_graph,current_keys)[0]:
                count_check_overlap +=1
        if count_check_overlap == len(rectangles):
            #for each rectangle the check_overlap returns True
            print ('all rectangles not overlaped')
            if self.check_emptiness(main_graph):
                return False #not a valid perfect rectangle
        else:
            return True


#Define the way of representation.
if __name__ == '__main__':
    #Examples return rectangles 1:
    rectangles = [[(1,1),(3,3)],[(3,1),(4,2)],[(3,2),(4,4)],[(1,3),(2,4)],[(2,3),(3,4)]]
    #TOCHECK
    #rectangles = [[(1,1),(2,3)],[(1,3),(2,4)],[(3,1),(4,2)],[(3,2),(4,4)]]

    current_graph = Rectangles()
    #print ('The state: empty of filled of the grid is:',current_graph.buildgraph(rectangles))

    #Check the results
    print ('Do the rectangles fit perfectly in the space:?',current_graph.complete_check(rectangles))

    #
