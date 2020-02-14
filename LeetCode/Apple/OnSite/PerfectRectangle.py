'''
Given N axis-aligned rectangles where N > 0, determine if they all
together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point.
For example, a unit square is represented as [1,1,2,2].
(coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
'''


'''
What are our thought patterns?
Lets look at Data structure:
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
Returns true
Data structure:
example: bottom-left point (1,1)
top-right (3,3)

Step 1: Find the  range of coordinates of x and y to iterate on.
min(x),max(x), min(y), max(y) In this case looping is done
over (1,1) until (4,4)--> min(x)=1, min(y)=1, max(x)=4, max(y)=4
Step 2: Just loop once.
#Check if the range is satisfied.
for rectangle in rectangles:
    #start with min(x)
    #Go in that rectangle to the upper right, rectangles[2]
    #if that value is not max(x):
    #Check if other rectangles have exactly the upper one or
    #loewer.

#Repeat the same for y
'''
class Solution:
    def isRectangleCover(self,rectangles)->bool:
        #Step 1: Find the min(x),max(x),min(y),max(y)

        check_global,check_x,check_y = False,False, False
        min_x=min([i[0] for i in rectangles]+[i[2] for i in rectangles])
        max_x=max([i[0] for i in rectangles]+[i[2] for i in rectangles])
        min_y=min([i[1] for i in rectangles]+[i[3] for i in rectangles])
        max_y=max([i[1] for i in rectangles]+[i[3] for i in rectangles])

        #Step 2. Check continuity range
        #Check ragne(x)
        for i in range(min_x,max_x):
            start = rectangles[0][0]
            end   = rectangles[0][2]
            for j in range(len(rectangles)):
                if start == min_x:
                    #check if rectangle[2]==max_x
                    if rectangles[j][2]==max_x:
                        check_x = True
                        return check_x
                    else:
                        #recursively check if another rectangle
                        #has the end
                        curr_end=rectangles[j][2]
                        while curr_end!=max_x:
                            if rectangles[j][2]==max_x:
                                checK_x = True
                                return checK_x
                        j+=1
                        check_x  = False
                        return checK_x

        #do it also for y.
        for i in range(min_y,max_y):
            start = rectangles[0][1]
            end   = rectangles[0][3]
            for j in range(len(rectangles)):
                if start == min_y:
                    #check if rectangle[2]==max_x
                    if rectangles[j][3]==max_y:
                        check_y = True
                        return check_y
                    else:
                        #recursively check if another rectangle
                        #has the end
                        curr_end=rectangles[j][3]
                        while curr_end!=max_x:
                            if rectangles[j][2]==max_x:
                                check_y = True
                                return check_y
                        check_y = False
                        return check_y
        return True if checK_x and check_y else False

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
output  = Solution()
print ("The rectangles cover is:",output.isRectangleCover(rectangles))
