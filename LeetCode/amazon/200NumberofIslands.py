#Code project from leet code

#Given a 2d grid map of '1's (land) and '0's (water), count the number of
#islands. An island is surrounded by water and is formed by connecting adjacent
#lands horizontally or vertically. You may assume all four edges of the grid
#are all surrounded by water.
#https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self,grid:List[List[str]])->int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        #approach: if there is point whose value is 1: exam its neighbours
        #top,bottom,left,right and count plus 1.

        m = len(grid)
        n = len(grid[0]) #number of columns

        #loop over the elements. Find our first 1 to search neighbourhood
        def check(i,j):
            if i < 0 or j< 0 or i==m or j==n or grid[i][j] != "1":
                return None

            grid[i][j] = "0"
            check(i-1,j)
            check(i+1,j)
            check(i,j-1)
            check(i,j+1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    check(i,j)
                    count +=1
        return count
if __name__ =='__main__':
    grid = [[11110],[11010],[11000],[00000]]
    object = Solution()
    count  = object.numIslands(grid)
