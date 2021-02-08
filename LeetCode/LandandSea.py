#Ref: LandandSea_v2.pdf
#
'''
Simplicity is the ultimate sophistication.


The question is about counting the number of islands.
Let's take a dive into simplifying the problem.

We define a 2D Map:
0s --> land
1s --> water

Search Problem --> DFS --> Dynamic Programming --> Recursive Call of the Function
'''

'''
Algorithmic Thinking

1. Define space 2D Map [[0 for i range(n)] for j in range(m)]
2. Initialise the spots where we have water.
2. Somehow loop over the map.
3. Loop:
    everytime we encounter a 0s or 1s we call a depth first search algorithm
    we keep track of the 4 neighbours: check(up,down,left,right)
    if all the checks are false, I move on else: I set the current cell
    to 1s and iteratively go the next one

    If condition breaks we update count by 1
'''

'''
Constraints:
'''

class Island():
    # start from point i and j to find this island scope
    def onboard(self,i, j,m,n):
        if i < 0 or j < 0 or i == m or j == n or map[i][j] != "1":
            return None

        map[i][j] = "0"
        self.onboard(i - 1, j,m,n)
        self.onboard(i + 1, j,m,n)
        self.onboard(i, j - 1,m,n)
        self.onboard(i, j + 1,m,n)

    def countIslands(self, map):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # approach: if there is a point whose value is 1, exam its neighbors and count plus one
        m = len(map)
        n = len(map[0]) if m else 0

        count = 0
        for i in range(m):
            for j in range(n):
                if map[i][j] == "1":
                    self.onboard(i, j,m,n)
                    count += 1

        return count

if __name__ == "__main__":
     map = [["1","1","0","0","0"], ["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
     #Object instantiation
     current_Island = Island()
     print (current_Island.countIslands(map))
