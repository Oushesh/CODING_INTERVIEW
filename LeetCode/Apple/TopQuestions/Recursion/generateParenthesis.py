#Generate Parenthesis.
#if we want to generate the Parenthesis:
#let's say N=3. 3 left and 3 right.
#Focus on your thought patterns

'''
Given n pairs of parenthesis, write a
function to generate all combinations
of well-formed parenthesis.
For example, given n=3, a solution set is:
'''

class Solution(object):
    def generateParenthesis(self,N):
        output = [] #to keep track of the results.
        S = ''
        open = 0
        closed = 0
        result=self.backtrack(output,N,S,open,closed)
        return result

    def backtrack(self,output,N,S,open,closed):
        if len(S)==2*N: #open and closed, here 3 open and 3 closed
            output.append(S)
        #in python we
        if open < N:
            #add left
            self.backtrack(output,N,S+'(',open+1,closed)
        if closed < open:
            #add right
            self.backtrack(output,N,S+')',open,closed+1)
        return output

'''
Interviewer asks you: what is the space and time complexity?
Time complexity: Use the catalan numbers
2n!/n!(n+1)
Space Complexity: worst case: O(n)
'''
if __name__ == "__main__":
    N = 3
    output  = Solution()
    print ('The resulting good combination of parenthesis is:',output.generateParenthesis(N))
