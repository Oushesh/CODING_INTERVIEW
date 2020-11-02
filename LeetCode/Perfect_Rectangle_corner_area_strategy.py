'''
@author: Oushesh Haradhun. In the light of carving the path to the United States of America.

This is a mock interview question from Leetcode called: Perfect_Rectangle_391.py

1. Take the given lower and upper corner points.
   Exapnd each of the rectangles.
   From 2 corners get all the 4 corners.

2. Store them as a set data structure. (Why: in python language its easier to eliminate
   common members of list if represented as set. Moreover set has O(1) time complexity
   for element lookup. Intersection and Union operations are way easier in set.)

3. Build 2 sets: - big_set() comprising of the 4 corner coordinates of external rectangle
                 - for each given

4. Iteratively find the for each of them if they have duplicates,
   remove them until the set is empty.

5. If the set is empty then: all of the subrectangles fit, otherwise not.

6.   Last but not least, we actually find if the area (overlap)

7. If there is no area overlap, and the set of corners is empty -->
   then the subrectangles form a perfect rectangle.

Lets walk the interviewer through it.

Example:
[(1,1),(3,3)],[(3,1),(4,2)],[(3,2),(4,4)],[(1,3),(2,4)],[(2,3),(3,4)]

rectangles = {A:[(1,1),(3,3)],
              B:[(3,1),(4,2)],
              C:[(3,2),(4,4)],
              D:[(1,3),(2,4)],
              E:[(2,3),(3,4)]}

lowest_left, upper_right

2 sets. Find the common in big_set and rectangle_set.
3. remove them from the list until list is empty.

4. Perform the operation area(rectangle) = sum(area of subrectangles)
5. If operation successful then success.
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
        area_big_rect = (upper_right[0]-lower_left[0])*(upper_right[1]-lower_right[1])
        sum_area_sub_rect = 0
        for rect in rectangles:
            width = rect[1][0]-rect[0][0]
            height = rect[1][1]-rect[0][1]
            current_area = width*length
            sum_area_sub_rect +=current_area

        if sum_area_sub_rect == area_big_rect:
            '''
            If this part is true then we have no overlap
            else not.
            '''
            return True
        return False

    def expand_corners(self,corners):
        '''
        example: (1,2),(3,5) --> becomes (1,2),(3,5),(1,5),(3,2)
        '''
        return [corners[0],corners[1],(corners[0][0],corners[1][1]),(corners[1][0],corners[0][1])]

    def recursive_set_delete(self,List_of_sets):
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
        resultant_set = List_of_sets[0]
        for i in range(1,len(List_of_sets)):
            resultant_set = resultant_set - List_of_sets[i]
        return resultant_set

    def check_corners(self,rectangles):
        upper_right, lower_left = self.upper_right_lower_left(rectangles)

        print ('Upper_right',upper_right)
        print ('lower_left',lower_left)

        #Update Big set with
        big_corners = [lower_left,upper_right]
        big_set = set(self.expand_corners(big_corners))
        all_sets = []

        for rect in rectangles:
            current_set = set(self.expand_corners(rect))
            all_sets.append(current_set)
        print ('List of sets:',all_sets)

        #now that we have all the sets we minus all
        #The check is good if we have empty set
        #Perform recursive function: setA - set B

        resultant_set = self.recursive_set_delete(all_sets)
        print ('resultant_set',resultant_set)
        if len(self.recursive_set_delete(rectangles))==0 and self.area_check(rectangles):
            #resultant set_is empty and there is no area overlap
            return True
        return False


if __name__ == '__main__':
    #First rectangle
    rectangles = [[(1,1),(3,3)],[(3,1),(4,2)],[(3,2),(4,4)],[(1,3),(2,4)],[(2,3),(3,4)]]
    #Second rectangle
    #rectangles = [[(1,1),(2,3)],[(1,3),(2,4)],[(3,1),(4,2)],[(3,2),(4,4)]]

    #'Call the function and print the result'
    current_rectangle = Rectangles()
    print ('The sub rectangles fit together:', current_rectangle.check_corners(rectangles))

    '''
    set_A = set([(1,1),(3,1),(1,3),(3,3)])
    set_B = set([(3,1),(3,2),(4,2),(4,1)])
    set_C = set([(3,2),(3,4),(4,2),(4,4)])
    set_D = set([(2,3),(3,4),(2,4),(3,3)])
    set_E = set([(1,3),(2,4),(1,4),(2,3)])
    set_A - set_B - set_C - set_D - set_E
    {(1, 2)}
    set_A = set([(1,1),(3,1),(1,3),(3,3)])
    set_A - set_B - set_C - set_D - set_E
    {(1, 1)}
    big_set = set([(1,1),(4,4),(1,4),(4,1)])
    set_A - set_B - set_C - set_D - set_E - big_set
    set()
    '''
