'''
Ref: https://www.geeksforgeeks.org/google-interview-experience-for-sde-1/?ref=rp

One chocolate bar is given. There are n number of pieces in that bar.
Each piece has its own sweetness level. You have to divide chocolate
bar in k pieces and give those pieces to k-1 persons and you will get
remaining last piece. You have to tell how much sweetness you will get.
You will get least sweetness piece out of all k pieces. So you have to
divide slab in such a way that you will get maximum sweetness.
Input: 1, 2, 4, 7, 3, 6, 9  N = 7, K = 4
Output: 7 (Divide it into 4 parts like [1, 2, 4] [7] [3, 6] [9] with sweetness level 7, 7, 9, 9 respectively)

Links for reference for similar problems:
https://www.geeksforgeeks.org/painters-partition-problem/
https://www.geeksforgeeks.org/allocate-minimum-number-pages/

Each number represents a given sweetness level:
'''

from collections import deque

class chocolate:
    def __init__(self,length,pieces):
        self.length = length
        self.pieces = pieces

    def sum(self,choco,start,end):
        total = 0
        for i in range(end):
            total+=choco[i]
        return total

    def get_max_sweetness(self):
        #Lets use dynamic programming here
        #dynamic programming. Lets build a 2D Array space
        #with the different ones here.

        #initialise the dynamic programming array here
        dp = [[0 for i in range(self.length+1)] for j in range(self.pieces+1)]

        for i in range(self.length+1):
            dp[1][i] = self.sum(choco,0,i-1)
        for i in range(self.pieces+1):
            dp[i][1] = choco[0]

        #The second case here.
        #2 to k partitions, 2 to n boards
        for i in range(2,self.pieces+1):
            for j in range(2,self.length+1):
                #I put the minimum to 0 but normally you
                best = 0
                for p in range(j):
                    best = min(best,max(dp[i-1][p],self.sum(choco,p,j-1)))
                    dp[i][j] = best
        return dp[self.pieces][self.length]

#This has cubic computational complexity.
#We can reduce it as follows: 

if __name__ == "__main__":
    choco = [1,2,4,7,3,6,9] #mychocolate
    pieces = 4
    length = len(choco)
    my_choco = chocolate(length,pieces)
    print ('The maximum sweetness you can get is:',my_choco.get_max_sweetness())

#TODO: I test my own approach as well and see what does it bring to us.

#TODO: the optimisation here.
