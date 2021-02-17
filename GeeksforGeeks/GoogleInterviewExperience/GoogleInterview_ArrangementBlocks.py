'''
You are given N blocks of height 1…N. In how many ways can you arrange these
blocks in a row such that when viewed from left you see only L blocks
(rest are hidden by taller blocks) and when seen from right you see
only R blocks? Example given N=3, L=2, R=1 there is only one arrangement
{2, 1, 3} while for N=3, L=2, R=2 there are two ways {1, 3, 2} and {2, 3, 1}

Height: 1,2,3, {2,1,3}
N=3, L=2, R=1

int output-> how many ways. (count)

From left I see only L Blocks(2)--> arrange in a way that every number after 2: 1 times greater.
[2,---,---] --> possibility 1: 2,3,1
                possibility 2: 2,1,3

R=1:  [1,2,3]
[1,2,3]
[2,1,3]

Indepentenly sort possibilities for Constraint 1, then for Constraint 2.

Find the intersecting possiblity that match both.

That was approach 1: Time Complexity: O(2n) Big O(notation): o(N)
                     Space Complexity: number of possibilities.


Can we do better? What if while

Example: 1,2,3,4,5,6
         from a sorted list we take n highest
         5,6,--,--,--,--
                      


leftmost 2 --> every number else has to be 3, rightmost

[2,]
This is an arrangement problem. or sorting problem
'''
if __name__ == "__main__":
