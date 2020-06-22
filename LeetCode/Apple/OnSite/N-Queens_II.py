'''
https://leetcode.com/problems/n-queens-ii/
The n-queens puzzle is the problem
of placing n queens on an nxn chessboard
such that no 2 queens attack each other.

Pseudocode:
Lets define some stuffs here:
0-- for positions where no queens
1-- valid positions for queens
such that no queen can attack each other.

Lets say n = 4
0 0 0 0         Q 1 1 1
0 0 0 0         1 1 0 0
0 0 0 0         1 0 1 0
0 0 0 0         1 0 0 1


A queen can attack in all directions (8-connected
components based, recursive search in the directions)
'''

class chessboard:
    def rule_checker(board):
        #Rule_checker basically takes in
        #generated scenarios for possible
        #solutions and rule them out.
        if
            return True
        return False
    def queens(self,n):
        #initialize the chessboard everywhere with zeros
        board = [[0 for j in n] for i in n]
        #Loop over the board to see eligibility of placing
        #the queens.

        return queens


if __name__ == "__main__":
