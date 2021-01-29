#Reference: https://www.geeksforgeeks.org/google-interview-experience-on-site-for-sde/

'''
Round 2:  https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/
It was something like this with a little variation that the total number of
moves were limited to a number t.
'''

'''
How do we solve this?

For this its easy: Lets solve it via dynamic programming:

lets save the possibilities with a 2D array:
Example:

1. 5,3,7,10: The user collects maximum value as 15(10+5).
2. 8,15,3,7: The user collects maximum value as 22(15+7).
   8,15,3,7 --> user=7, opponent=8,user chooses
   opponent is not an idiot: max(current_first, current_last)

   User chooses

We define a map array --> 8,15,3,7

User: 8
Opponent: 15

User: 7
Opponent: 3

Resultant: Opponent --> 15+3 = 22, User --> 8+7= 15
max(opponent,user) So if the user is not stupid --> user takes maximum of
either front or back at each level.

As we loop keep track of the player:
player = user (at the beginning)
if player: user= opponent, else: player= user
at each loop iteration keep track of the current_head or current_tail:
last = last-1 if someone chooses last
front = front+1

We know user always starts first: U-User, O-opponent
  8   15   3    7
  U                     max(8,7) --> 8, user.append(8)
  U   O

In the end the solution is just: max(sum(oppponent),sum(user))
Then we have it. Lets code!!!

This is linear!!

Case 2: In Case the user or

This one is in a new case when the user or opponent is not necessarily intelligent,
--> implies user or opponent may or may not take the max out of the current left most or right most element.

We build a tree for each possibility like a tree, then traverse the tree to go sum
all nodes from the same path. --> Draw the tree here
'''

#One easy version. If both players are definitely not stupid --> every decision that you take is definite. Its linesr
import collections
from collections import deque

class CoinGame:
    def __init__(self,coins):
        self.coins = coins
        self.turn = None   #self.turn can take 2 variables: 'U' for user and 'o' for opponent
        self.user = []
        self.opponent = []
        self.current = None

    def count(self,coins):
        self.turn = 'u'
        #convert coins to deque in Python for more computational efficieny.
        #List: pop(index)--> O(n) complexity, popleft or popright of deque has O(1) time complexity
        #We will only take the leftest or rightest.
        coins = deque(coins)
        while len(coins)>0:
            if coins[0] > coins[-1]:
                self.current = coins.popleft()
            else:
                self.current = coins.pop()  #pop means popright()

            if self.turn =='u':
                self.user.append(self.current)
                self.turn = 'o'
            elif self.turn == 'o':
                self.opponent.append(self.current)
                self.turn = 'u'

        return max(sum(self.user),sum(self.opponent))


        '''
        How we want the output to look like
        len(combinations) = len(coins)*2
        len(combinations) = len(combinations)/2

       [0    1  3   4]
        8   15  3   7
        U    O  U   O
        U    O  O   U
        U    u  o   O
        U    o  u   O
        O    u  o   U
        O    0  U   U
        U    o  O   U
        o    U  O   U
        '''

    '''
    Updated: 26.01.2021
    '''
     #In Case the user or gamer is not intelligent, which means we have
     #more conditions. The system is probabilistic & not definite.
     #We thus build the above the preprocessing table to account for
     #all the possible paths of the system.
     #3. Keep track of sum of all possible paths & max of those sums


    #Actually each row represents a
    #Path is sum along the row.
    #Each path is unique.
    #max(sum(path))
    def preprocess(self,coins):
         self.turn = 'u'  #the first turn for the user is always 'u', then sequential alternative: 'u' and 'o'
         combinations = len(coins)*2  #2players thats why.
         grid = [0 for i in range(len(coins))] for j in range in combinations]

         print ('grid initialised:',grid)

         repeat = len(combinations)//2 #integer output #4
         indices = deque([i for i in range(len(coins))]) #the reason why we use deque is because we efficiently pop left and pop right with a time complexity O(1)


        #Pop both sides until indices does not exist.
        #We exhaused all moves
        while (indices):
            front = indices.popleft() #0
            back  = indices.pop() #3
            while (repeat>=1):
                #Here repeat is 4.
                for i in range(repeat):
                    grid[i][front]= 'u' #(0,0), (0,1), (0,2), (0,3)
                    grid[]
                repeat//=2

         return grid


    def max_paths(self,grid):

            return max


###TODO: write a readme

if __name__ == "__main__":
    coins = [8,15,3,7] #input coins, 2 players: user, opponent.

    currentGame = CoinGame(coins)

    print ('The max count of the number of coins is:',currentGame.count(coins))

    #Case 2: One or both players can be stupid. --> much more complicated. preprocess using a 2D Array
