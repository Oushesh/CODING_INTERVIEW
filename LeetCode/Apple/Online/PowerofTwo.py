'''
Apple online mock interview:
Given an integer, write a function to determine if it is
a power of two.
Example 1:
Input: 1
output: True
Explanation: 2° = 1
'''

class Solution:
    def isPowerOfTwo(self,n):
        if n==0:
            return False
        while n% 2 == 0:
            n /=2
        return n==1

if __name__ == "__main__":
    Input = 16
    object=Solution
    print ('Is the number divisible by 2?',object.isPowerOfTwo(Input))
