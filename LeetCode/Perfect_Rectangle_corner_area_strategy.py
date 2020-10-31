'''
1. Take the given lower and upper corner points.
   Exapnd each of the rectangles. From 2 corners get all the 4 corners

2. Store them as a set data structure.

3. Build 2 sets 1 for the lower left and upper right

4. Iteratively find the for each of them if they have duplicates,
   remove them until the set is empty.

5. If the set is empty then: all of the subrectangles fit, otherwise not.

6.   Last but not least, we actually find the overlap.

Lets walk the interviewer through it.

Example:
[(1,1),(3,3)],[(3,1),(4,2)],[(3,2),(4,4)],[(1,3),(2,4)],[(2,3),(3,4)]

rectangles = {A:[(1,1),(3,3)],
              B:[(3,1),(4,2)],
              C:[(3,2),(4,4)],
              D:[(1,3),(2,4)],
              E:[(2,3),(3,4)]}

lowest_left, upper_right


'''


if __name__ == '__main__':
    #First rectangle
    rectangles = [[(1,1),(3,3)],[(3,1),(4,2)],[(3,2),(4,4)],[(1,3),(2,4)],[(2,3),(3,4)]]
    #Second rectangle
    rectangles = [[(1,1),(2,3)],[(1,3),(2,4)],[(3,1),(4,2)],[(3,2),(4,4)]]

    #'Call the function and print the result'
