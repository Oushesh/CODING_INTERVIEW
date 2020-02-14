'''
8 houses, represented as cells, are arranged in a straight line.
Each day every cell competes with its adjacent cells.

An value of 1 represents an active cell and a value of 0 represents an inactive
cell.
If the neighbours on both sides of a cell are active or inactive, the cell becomes
inactive the next day; otherwise the cell becomes an active cell.

The 2 cells on each end have a single adjacent cell, so assume the unoccupied
space on opposide is an inactive cell.
Eveen after updating the cell state, consider its previous state when
updating the state of other cells. The state information of all cells
should be updated simultanouesly.


Write an algorithm to output the state of the cells after the
given number of days.

Input:
The input to the function/method consists of  2 argumentss:
states,
list of integers representing current state of cells:
days, int. representing the number of days.

Output:
Return a list of integers representing the state of the cells
after the given n days.

Test Case:
[1,0,0,0,0,1,0,0], 1
Expected Value:
[0,1,0,0,1,0,1,0]

Test Case 2:
[1,1,1,0,1,1,1,1], 2
[0,0,0,0,0,1,1,0]
'''

'''
Thought Process:

[1,0,0,0,0,1,0,0] --> 0,1,0,0,0,0,1,0,0,0

model this rule: cell[i] in range(len(cell)) -->
if cell[i-1] and cell[i+1] == 0 or cell[i-1] and cell[i+1]==1
'''
class Solution:
    def cellComplete(self,cells,days):
        #initialize a 2D array
        dp = [[1 for i in cells] for j in range(days+1)]
        dp[0]=cells #initialize with the day 0 given as cells
        for d in range(1,len(dp)):
            for c in range(1,len(dp[0])-1):
                #write the update rule here:s
                if c==0:
                    if dp[d-1][c+1]==0:
                        dp[d][c] = 0
                if c==len(dp[0]):
                    if dp[d-1][c]==0:
                        dp[d][c] = 0 #check the conditions here
                elif (dp[d-1][c+1]==0 and dp[d-1][c-1]==0) or (dp[d-1][c+1]==1 and dp[d-1][c-1]==1):
                    dp[d][c] = 0
        return dp[-1]

if __name__ == "__main__":
    cells = [1,0,0,0,0,1,0,0]
    days  = 1
    output = Solution()
    print ('The cells afterwards are:',output.cellComplete(cells,days))
