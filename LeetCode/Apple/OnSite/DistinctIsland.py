#Given a non-empty 2D array grid of 0's and 1's, an island is a group of
# 1's (representing land) connected 4-directionally (horizontal or vertical.)
#You may assume all four edges of the grid are surrounded by water.

#Count the number of distinct islands. An island is considered to be the same
 #as another if and only if one island can be translated (and not rotated or
 #reflected) to equal the other.

class Solution:
    def numDistinctIsland(self,grid:[List[List[int]]]) -> int:
        x = len(grid)
        y = len(grid[0])


        return count

if __name__ == '__main__':
    grid = [[11000],[11000],[00011],[00011]]
    object = Solution()
    object.numDistinctIsland(grid)
