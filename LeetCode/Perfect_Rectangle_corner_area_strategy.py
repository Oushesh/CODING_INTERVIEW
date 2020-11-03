'''
@author: Oushesh Haradhun. In the light of carving the path to the United States of America.

This is a mock interview question from Leetcode called: Perfect_Rectangle_391.py
This question is really famous for apple software engineering roles.
It involves Geometrical understanding and some important data structure
understanding.

My proposal:

Based on the constraint given:
We cannot have overlap nor empty spaces left by the subrectangles inside
the main big rectangle.

So thus:
Check that sum(area of subrectangles) equals area of main rectangle.

Then check overlapping corner points.

1. Take the given lower and upper corner points.
   Exapnd each of the rectangles.
   From 2 corners get all the 4 corners.

2. Store them as a set data structure. (Why: in python language its easier to eliminate
   common members of list if represented as set. Moreover set has O(1) time complexity
   for element lookup. Intersection and Union operations are way easier in set.)

3. Build 2 sets: - big_set() comprising of the 4 corner coordinates of external rectangle
                 - for each given rect in the given rectangle data:
                    expand the 2 coordinates to  4 and get all 4 of them.
                    add it to a list of set data structure.

4. Combine the big_set and list of sets of subrectangle coordinates into a big list
   of sets.

5. Then perform sets subraction. --> set subraction = removing common coorindate
   pairs in the sets. Mathematically it means if the rectangles fit exactly,
   all the coordinate pairs have to have pairs and commons.

5. If the set is empty then: all of the subrectangles fit, otherwise not.

6.   Last but not least, we actually find if the area (overlap)

7. If there is no area overlap, and the set of corners is empty -->
   then the subrectangles form a perfect rectangle.
'''

class Rectangles():
    def upper_right_lower_left(self,rectangles):
        '''
        returns the upper right and lower left corners
        type: (1,1), (4,4)
        '''
        upper_right = min(min([rect[0] for rect in rectangles],[rect[1] for rect in rectangles]))
        lower_left  = max(max([rect[0] for rect in rectangles],[rect[1] for rect in rectangles]))
        return upper_right, lower_left

    def area_check(self,rectangles):
        '''
        returns boolean whether sum area of subrectangles
        = area of bigger rectangle
        '''
        upper_right, lower_left = self.upper_right_lower_left(rectangles)
        area_big_rect = (upper_right[0]-lower_left[0])*(upper_right[1]-lower_left[1])
        sum_area_sub_rect = 0
        for rect in rectangles:
            width = rect[1][0]-rect[0][0]
            height = rect[1][1]-rect[0][1]
            current_area = width*height
            sum_area_sub_rect +=current_area

        if sum_area_sub_rect == area_big_rect:
            '''
            If this part is true then we have no overlap
            else not.
            '''
            return True
        else:
            return False

    def expand_corners(self,corners):
        '''
        example: (1,2),(3,5) --> becomes (1,2),(3,5),(1,5),(3,2)
        '''
        return [corners[0],corners[1],(corners[0][0],corners[1][1]),(corners[1][0],corners[0][1])]

    def recursive_set_delete(self,list_set):
        #all_sets: list of sets
        '''
        recursively delete elements in the list of sets
        list of sets:
        [
            {(1, 3), (2, 3), (1, 1), (2, 1)},
            {(1, 3), (2, 3), (2, 4), (1, 4)},
            {(4, 2), (3, 2), (3, 1), (4, 1)},
            {(4, 2), (3, 2), (4, 4), (3, 4)}
        ]
        '''

        output_set = list_set[0]
        for i in range(1,len(list_set)):
            print ('index',i,'resultant_set',output_set)
            output_set = output_set - list_set[i]
        return output_set

    def check_corners(self,rectangles):
        upper_right, lower_left = self.upper_right_lower_left(rectangles)

        #Update Big set with
        big_corners = [lower_left,upper_right]
        big_set = set(self.expand_corners(big_corners))
        all_sets = []
        for rect in rectangles:
            current_set = set(self.expand_corners(rect))
            all_sets.append(current_set)
        all_sets.append(big_set)
        #now that we have all the sets we minus all
        #The check is good if we have empty set
        #Perform recursive function: setA - set B

        resultant_set = self.recursive_set_delete(all_sets)

        if len(resultant_set)==0:
            print ('corners fit perfectly together')
            if self.area_check(rectangles):
                #resultant set_is empty and there is no area overlap
                return True
        else:
            return False

if __name__ == '__main__':
    #First rectangle
    rectangles = [[(1,1),(3,3)],[(3,1),(4,2)],[(3,2),(4,4)],[(1,3),(2,4)],[(2,3),(3,4)]]

    #Second rectangle
    #rectangles = [[(1,1),(2,3)],[(1,3),(2,4)],[(3,1),(4,2)],[(3,2),(4,4)]]

    #'Call the function and print the result'
    current_rectangle = Rectangles()
    print ('The sub rectangles fit together:', current_rectangle.check_corners(rectangles))
