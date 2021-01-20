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
        print (self.user, self.opponent)
        return max(sum(self.user),sum(self.opponent))


    '''
    This one is in a new case when the user:
    '''
if __name__ == "__main__":
    coins = [8,15,3,7] #input coins, 2 players: user, opponent.

    currentGame = CoinGame(coins)
    print (currentGame)
    print ('The max count of the number of coins is:',currentGame.count(coins))

#Case 2: One or both players can be stupid. --> much more complicated. preprocess using a 2D Array
