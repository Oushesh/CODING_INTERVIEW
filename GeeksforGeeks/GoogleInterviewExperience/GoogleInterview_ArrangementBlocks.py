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

Approach 1:
Indepentenly sort possibilities for Constraint 1, then for Constraint 2.

Find the intersecting possiblity that match both.

That was approach 1: Time Complexity: O(2n) Big O(notation): o(N)
                     Space Complexity: number of possibilities.


Approach 2:
Can we do better? What if while if we try something else:

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

    def permute_iterative(self,num_constraint):
        '''
        return number of permutations
        '''
        number = num_constraint
        while (number>0):
            output=number*number-1
            number-=number
        return output

    def permute(self,num_constraint):
        '''
        return permutation of a given number
        Mechanism of permutation is like this:
        Here we just to recursive call:
        output! = len(blocks)-num_constraint
        2 ways to make it: Iterative but I prefer recursive
        5*4*3*2*1
        '''
        if num_constraint==1:
            return num_constraint
        return num_constraint*self.permute(num_constraint-1)


    def rearrange(self):
        #Edge case: L and R cannot be the same
        assert(not L==R)
        #The other edge case is also to check
        assert (L+R < len(self.blocks))

        if (not self.blocks==sorted(self.blocks)):
            self.blocks = sorted(self.blocks) #sorted with the min on the left and max on the right

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
        #If we had no constraint and we were to arrange the elements without repetition
        # number of combinations = len(blocks)!
        #We have a constraint num_constraint = L+R
        #ouput = len(block) - num_constraint
        #permutation(output)= answer

        num_constraint = len(self.blocks)+1-(minimum+second)

        print ('num_constraint',num_constraint)
        print ('second',second)
        return self.permute_iterative(num_constraint)

        #TODO: extend the question to even give the output here:


if __name__ == "__main__":
    L = 2
    R = 1
    blocks = [1,2,3,4,5,6]

    #Unit test check input
    assert(isinstance(L,int))
    assert(isinstance(R,int))
    assert(isinstance(blocks,list))
    current_arrangement = arrangement(L,R,blocks)
    print ('The number of arrangements so one can see blocks based on the constraint given is:',current_arrangement.rearrange())

    #Using the recusive formulation here:
    print ('The number of arrangements so one can see blocks based on the constraint given is:',current_arrangement.rearrange())

'''
Example: After coding walking the interview just to check (Google Style interview)

We have 2 Left Constraint & 1 Right constraint:
minimum = right
second = left
Because the right one being minimum is highest: we will already
see it from the left side. Cannot block it.

'''
