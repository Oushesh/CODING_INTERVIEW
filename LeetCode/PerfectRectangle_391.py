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
    def buildgraph(self,rectangles):
        #find lowest left and most upper right coordinate
        lowest_left = min(min([rect[0] for rect in rectangles],[rect[1] for rect in rectangles]))
        upper_right = max(max([rect[0] for rect in rectangles],[rect[1] for rect in rectangles]))
        #loop initialise with 0s
        graph = {}
        for i in range(lowest_left):
            graph[] =

        return graph




if __name__ = '__main__':
    #Examples return rectangles 1:
    rectangles = [[(1,1),(3,3)],[(3,1),(4,2)],[(3,2),(4,4)],[(1,3),(2,4)],[(2,3),(3,4)]]

    current_graph = 
    print ('The state: empty of filled of the grid is:',)
