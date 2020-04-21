#Reference: https://leetcode.com/problems/perfect-rectangle/

'''
Given N axis-aligned rectangles where N> 0,
determine if they all together form an exact
cover of a rectangular region.
'''

'''
Thought Strategies:

Check the corner points:
Bottom Left: BL
Bottom Right: BR
Top Left: TL
Top Right: TR

1. Step 1: From the rectangles: Get BL,BR,TL,TR
2. Step 2: Check that corners only Touch. No overlap

3. Loop from min. x to max x.
(1,1) --> (1,3) (same rectangle) (max of current rectangle)
(1,3) --> search if we have

Breadth First Technique
(1,1) --> (1,3) --> (3,3) (no conenection here)
      --> (3,1) --> (3,3)

(1,3) --> ()

'''

class PerfectRectangle:
    def check_corner(self):
        return None


if __name__ == "__main__":
    rectangles = [[1,1,3,3],
    [3,1,4,2],
    [3,2,4,4],
    [1,3,2,4],
    [2,3,3,4]]
