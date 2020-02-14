#2D stuffs, number of islands

#Recusrion problem on 2D Space
#Greedy Approach:
#First search for fitst alphabet.
#mark it as found. -->0
#then recursively search left,right,up, down, and propagate the search

#Amazon Coding interview

class my_Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #edge cases
        if len(board)== 0 or len(board[0])==0:
            return False

        #loop over the board and check for matches with word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(board,i,j,word,0):
                    return True
        #If i continue from here:
        #then the function check has to continue checking, up,left,right
        #down like a depth first search

    def check(self,board,i,j,word,current):
        #check the edge cases.
        #we know also we need to mark visited places.
        if current == len(word):
            return True
        elif i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]=='-1':
            return False
        else:
            #Update the coordinates
            if board[i][j]== word[current]:
                temporary = board[i][j]
                board[i][j]='-1'
                #call the function check for up,down,left,right positions
                checked = self.check(board,i-1,j,word,current+1) or self.check(board,i+1,j,word,current+1) or self.check(board,i,j+1,word,current+1) or self.check(board,i,j-1,word,current+1)
                board[i][j]= temporary
                return checked
            else:
                return False

#Space and time complexisty: Recursive solution: O()
#Space complexity:
if __name__ == "__main__":
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
word = "ABCCEDS"
output = Solution()
print (output.exist(board,word))
