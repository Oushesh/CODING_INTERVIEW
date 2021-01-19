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
'''
