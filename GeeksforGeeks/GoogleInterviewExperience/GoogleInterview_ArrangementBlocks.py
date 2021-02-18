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


#Let's do it for Google!
class arrangement:
    def __init__(self,L,R,blocks):
        self.L = L
        self.R = R
        self.blocks = blocks

    def rearrange(self):
        #Edge case: L and R cannot be the same
        assert(not L==R)
        #The other edge case is also to check
        assert (L+R == len(self.blocks))

        if (not blocks==sorted(blocks)):
            blocks = sorted(blocks) #sorted with the min on the left and max on the right

        '''
        if L=2, R=1 --> From right I can only seen 1 block across., From left
        I can only see 2 blocks across.
        '''
        #We take the minimum from L and R
        minimum = min(L,R)
        #second is just not the min.
        second = max(L,R)
        second-=1

        #Write a way to write number of combinations





if __name__ == "__main__":
    L =
    R =
    blocks

    #Unit test check input
    assert(L==int)
    assert(R==int)
    assert(is_instance(blocks,list))

    print ('The number of arrangements so one can see blocks based on the constraint given is:',)
