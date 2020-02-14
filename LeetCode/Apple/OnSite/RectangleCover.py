#Given N axis-aligned rectangles where N > 0, determine if they all together
#form an exact cover of a rectangular region.

#Each rectangle is represented as a bottom-left point and a top-right point.
# For example, a unit square is represented as [1,1,2,2]. (coordinate of
#bottom-left point is (1, 1) and top-right point is (2, 2)).

def check_connectivity(min,max,list1,list2):
    for i in range(c):
        if grid[0][i] < max_x:
            anchor_x = max_x
            if anchor_x in x1 or if anchor_x in x2:
                position = np.where(anchor_x==x1 or anchor_x==x2)
                #Find if x2 of that rectangle is
                final_point = x2[position]
            else:
                return False #Disconnected

class Solution:
    def isRectangleCover(self,rectangles: List[[List[int]]]) -> bool:
        r = len(grid)
        c = len(grid[0])

        #Find starting point
        #loop over the range from min_x, max_x
        #Find the rectangle whose x1 or x2 lies there.

        x1     = [grid[i][0] for i in range(r)]
        x2     = [grid[i][2] for i in range(r)]
        y1     = [grid[0][i] for i in range(c)]
        y2     = [grid[2][i] for i in range(c)]

        min_x = grid[0][0]
        max_x = min([i for i in grid[i][0]],[i for i in grid[i][2]])
        #Call check connectivity # bottom x, top x, left and right
        for i in range (r):
            if x1[i] < max_x:
                anchor = x1[i]
                if x2[i] < max_x and x2[i]!=max_x:
                    anchor = x2[i]

    return True



if __name__ == "__main__":
    #Format is [x1,y1,x2,y2]
    rectangles= rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
    object = Solution()
    print (object.isRectangleCover(retangles))
